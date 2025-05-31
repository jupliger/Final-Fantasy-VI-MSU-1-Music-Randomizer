#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {

    // Check usage
    if (argc < 2 || argc > 3) {
        printf("\nUsage: msu2wav INPUT [OUTPUT]\n");
        return 0;
    }

    // Open the input file
    FILE *msufile;
    msufile = fopen(argv[1], "rb");
    if (msufile == NULL) {
        perror("\nInput file");
        return -1;
    }

    // Determine the length
    fseek(msufile, 0, SEEK_END);
    unsigned int msulen = ftell(msufile);
    unsigned int wavlen = msulen - 8;
    rewind(msufile);

    if (msulen < 12) {
        printf("Input file does not contain any samples.\n");
        return -2;
    }
    
    // Check for MSU1 signature
    char msu_sig[] = "MSU1";

    for (int i = 0; i < 4; i++) {
        if (fgetc(msufile) != msu_sig[i]) {
            printf("Invalid input file.\n");
            return -3;
        }
    }

    // Open output file
    char outname[255];

    if (argc == 2) {
        strcpy(outname, argv[1]);
        strcat(outname, ".wav");
    }
    else {
        strcpy(outname, argv[2]);
    }

    printf("Saving %s...", outname);
    FILE *wavfile = fopen(outname, "wb");

    if (wavfile == NULL) {
        perror("\nError");
        return -4;
    }

    /*
    All values below assume the standard MSU1 audio format.
    This should be 16-bit stereo PCM with a sample rate of 44100.
    */

    unsigned int s_rate = 44100;
    unsigned int b_rate = s_rate * 2 * 2;
    unsigned char msu[44];

    msu[0]  = 'R'; // Chunk ID
    msu[1]  = 'I';
    msu[2]  = 'F';
    msu[3]  = 'F';
    msu[4]  = (wavlen+36); // Chunk Size
    msu[5]  = (wavlen+36) >> 8;
    msu[6]  = (wavlen+36) >> 16;
    msu[7]  = (wavlen+36) >> 24;
    msu[8]  = 'W'; // Format
    msu[9]  = 'A';
    msu[10] = 'V';
    msu[11] = 'E';
    msu[12] = 'f'; // Subchunk 1 ID
    msu[13] = 'm';
    msu[14] = 't';
    msu[15] = ' ';
    msu[16] = 16; // Subchunk 1 Size
    msu[17] = 0;
    msu[18] = 0;
    msu[19] = 0;
    msu[20] = 1; // Audio Format
    msu[21] = 0;
    msu[22] = 2; // Num Channels
    msu[23] = 0;
    msu[24] = s_rate; // Sample Rate
    msu[25] = s_rate >> 8;
    msu[26] = 0;
    msu[27] = 0;
    msu[28] = b_rate; // Byte Rate
    msu[29] = b_rate >> 8;
    msu[30] = b_rate >> 16;
    msu[31] = b_rate >> 24;
    msu[32] = 4; // Block Align
    msu[33] = 0;
    msu[34] = 16; // Bits Per Sample
    msu[35] = 0;
    msu[36] = 'd'; // Subchunk 2 ID
    msu[37] = 'a';
    msu[38] = 't';
    msu[39] = 'a';
    msu[40] = wavlen; // Subchunk 2 Size
    msu[41] = wavlen >> 8;
    msu[42] = wavlen >> 16;
    msu[43] = wavlen >> 24;

    // Write header
    if (fwrite(msu, 1, 44, wavfile) != 44) {
        printf("Error writing WAV header\n");
        return -5;
    }

    // Write data
    int default_size = 1024;
    int buffer_size;
    fseek(msufile, 8, SEEK_SET);
    do {
        buffer_size = (msulen - ftell(msufile) > default_size) ? default_size : wavlen % default_size;
        unsigned char buffer[buffer_size];
        if (fread(buffer, 1, buffer_size, msufile) != buffer_size) {
            printf("Error reading WAV data\n");
            return -6;
        }
        if (fwrite(buffer, 1, buffer_size, wavfile) != buffer_size) {
            printf("Error writing WAV data\n");
            return -7;
        }
    } while (buffer_size == default_size);


    fclose(msufile);
    fclose(wavfile);
    printf("Done!\n");
    return 0;

}