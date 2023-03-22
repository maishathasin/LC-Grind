class Solution {
 public List<Integer> countSmaller(int[] nums) {
    List<Integer> integerList = new ArrayList<>();
    int count;
    for (int i = 0; i < nums.length; i++) {
        count = 0;
        for (int n = i + 1; n < nums.length; n++) {
            if (nums[n] < nums[i]) {
                count++;
            }
        }
        integerList.add(count);
    }
    return integerList;
}
}