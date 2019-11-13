#include<stdio.h>
#include<stdlib.h>
#include<omp.h>

//static long num_steps  = 100000;
double step, stime, etime,total;

int main(int n,char *a[])
{
        int i,t = atoi(a[1]);
        printf("%d\n",t);
        double x,pi,sum=0.0;
        long num_steps = atol(a[2]);
        step = 1.0/(double)num_steps;
        
        for(int j=1;j<=100;j++)
        {
            sum=0.0;
            stime = omp_get_wtime();
            
            //printf("No. of threads: %d  ",j);
            omp_set_num_threads(t);
            #pragma omp parallel for reduction(+:sum) private(x)
            for(i=0;i<num_steps;i++)
            {
                x = (i+0.5)*step;
                sum  = sum + 4.0/(1.0+x*x);
            }
            pi = step*sum;
            etime = omp_get_wtime()-stime;
            //total+=etime;
            //printf("pi value = %.16g  ",pi);
            //printf("time = %lf\n",etime);
           
        }
         printf("Avgtime = %lf\n",etime);
        return 0;
}
