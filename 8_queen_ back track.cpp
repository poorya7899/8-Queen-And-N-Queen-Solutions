#include<iostream>
#include<string.h>
using namespace std;

#define size 8
int arr[size];

// is there any conflict in array
bool heuristic(int index){
	for(int i=1 ; i<=index ; i++){
		if((arr[index]-i == arr[index-i]) |
			(arr[index]+i == arr[index-i])|
			(arr[index] == arr[index-i])) {
				return false;
		}
	}
	return true;
}

// fill board by back track algorithm
bool build(int index){
	// check array is filled or not
	if(index < size){
		// fill this index from 0 to size-1 , check heuristic
		for(int i=0 ; i<size ; i++){
			arr[index] = i;
			if(heuristic(index)){
				build(index+1);
			}
		}
	}
	else{
		// resault find , print it
		for(int i=0 ; i<size ; i++){
			cout<<arr[i]<<" ";
		}
		exit(1);	
	}
}

// main function
int main(){
	memset(arr,-1,sizeof(arr));
	build(0);
}
