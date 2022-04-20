#include <time.h>
#include <stdio.h>

int main()
{
    clock_t tic = clock();

    for (int n = 1; n < 80; n++)
    {
        int sqn = n * n;
        for (int a = 1; a < n; a++)
        {
            int sqa = a * a;
            for (int b = a - 1; b < n; b++)
            {
                int sqb = sqa + b * b;
                if (sqb > sqn)
                {
                    break;
                }
                for (int c = b - 1; c < n; c++)
                {
                    int sq = sqb + c * c;
                    if (sq > sqn)
                    {
                        break;
                    }
                    if (sq == sqn)
                    {
                        printf("%d %d %d %d\n", a, b, c, n);
                    }
                }
            }
        }
    }

    clock_t toc = clock();

    printf("Elapsed: %lf seconds\n", (double)(toc - tic) / CLOCKS_PER_SEC);

    return 0;
}
// same code on python execs in 0.87
// timing 0.003