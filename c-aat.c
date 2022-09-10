#include <stdio.h>
void main()
{
    int n,d,h,l ;
    int i ;
    int ai[50] ;
    l = 0 ;
    printf("Enter the total number of days,max level,d:\n") ;
    scanf("%d %d %d",&n,&h,&d) ;
    printf("Enter amountS of rain\n") ;
    for(i=0;i<n;i++)
    {
        scanf("%d",ai+i) ;
    }
    for(i=0;i<n;i++)
    {   
        if (ai[i]>0) 
            l += ai[i] ;
        else if (ai[i]==0)
            l -= d ;

        if (l>h) 
        {
            printf("Red Alert on day %d\n",i+1) ;
            i = 100 ;
            break ;
        }
        if (l<d)
            l = 0 ;
    }
    if (i!=100)
        printf("No red alerts\n") ;
}