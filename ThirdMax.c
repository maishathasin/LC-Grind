

int thirdMax(int* nums, int numsSize) {
    int max1=INT_MIN;
    int max2=INT_MIN;
    int max3=INT_MIN;
    int count=0;
    for(int i=0;i<numsSize;i++){
        if(max1<=nums[i]){
           max1=nums[i]; 
        }
    }
    for(int i=0;i<numsSize;i++){
        if(max2<=nums[i]&&nums[i]<max1){
            max2=nums[i];
        }  
    }
    for(int i=0;i<numsSize;i++){
        if(max3<=nums[i]&&nums[i]<max2){
            max3=nums[i];
            count++;
        } 
    }
    if(count==0){return max1;
                }
    return max3;
}