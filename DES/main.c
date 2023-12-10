#include <stdio.h>

void find_max(int num[], int *max);
void find_min(int num[], int *min);

int main()
{
    int num[10] = {9, 7, 6, 12, 44, 53, 32, 11, 29, 20};
    int max = num[0];
    int min = num[0];

    find_max(num, &max);
    find_min(num, &min);

    printf("max=%d, min=%d\n", max, min);

    return 0;
}

void find_max(int num[], int *max)
{
    int i = 0;
    for (i = 0; i < 10; i++)
    {
        if (num[i] > *max)
        {
            *max = num[i];
        }
    }
}

void find_min(int num[], int *min)
{
    int i = 0;
    for (i = 0; i < 10; i++)
    {
        if (num[i] < *min)
        {
            *min = num[i];
        }
    }
}
