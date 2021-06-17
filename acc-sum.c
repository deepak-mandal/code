#include<stdio.h>
int main(){
	
	int n, i;
	int sum;
	scanf("%d", &n);
	for (i=1; i<=10; i++){
		printf("%d ", i*n);
		sum+=i*n;
	}
	printf("\n");
	printf("%d ", sum);
	
	
	
	
	return 0;
}
