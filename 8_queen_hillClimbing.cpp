#include<iostream>
#include<string.h>
#include<stdlib.h>
#include<time.h>
#include<set>
using namespace std;

#define size 8
int counter = 0;

// find number of conflict
int heuristic(int arr[]){
	int faults = 0;
	for(int index = 0 ; index < size ; index++){
		for(int i=1 ; i<=index ; i++){
			if((arr[index]-i == arr[index-i]) |
				(arr[index]+i == arr[index-i])|
				(arr[index] == arr[index-i])) {
					faults++;
			}
		}
	}
	return faults;
}

// fill array with 0 to size-1 with random arrange
void build(int arr[]){
	// build set of numbers from 0 to size-1
	set<int> nums;
	set<int>::iterator it;
	int temp;
	for(int i=0 ; i< size ; i++){
		nums.insert(i);
	}
	// arrange numbers
	for(int i= size ; i > 0 ; i--){
		srand(++counter);
		temp = rand()%i;
		for(it = nums.begin() ; temp >0 ; it++){
			temp--;
		}
		arr[i-1] = *it;
		nums.erase(it);
	}
}

int main(){
	// minimum resault and next map variables
	int min_h , temp_h;
	int min_res[size] , temp_res[size];
	// build first map
	build(min_res);
	min_h = heuristic(min_res);
	// do this while conflicts > 0
	while(min_h != 0){
		// build next map
		build(temp_res);
		temp_h = heuristic(temp_res);
		// is better?
		if(min_h > temp_h){
			// copy it
			min_h = temp_h;
			for(int i=0 ; i< size ; i++){
				min_res[i] = temp_res[i];
			}
		}
	}
	// print resault
	for(int i=0 ; i< size ; i++){
		cout<<temp_res[i]<<" ";
	}
}
