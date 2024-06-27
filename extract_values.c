#include <math.h>
#include <stdio.h>
#include <stdint.h>

#define M_PI 3.14159265358979323846264338327950288

int main(void)
{
    printf("const int16_t cos_lookup1[]={");
    for(float i = 0.0; i < 256; i++)
        printf("%d,", (int16_t)(10000*cos(M_PI*i/512)));
    printf("\b}\n");
    return 0;
}