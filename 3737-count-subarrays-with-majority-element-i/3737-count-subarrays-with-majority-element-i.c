int countMajoritySubarrays(int* nums, int numsSize, int target) {
    int ans = 0;

    for (int i = 0; i < numsSize; i++) {
        int cnt = 0;

        for (int j = i; j < numsSize; j++) {
            if (nums[j] == target)
                cnt++;

            if (cnt * 2 > (j - i + 1))
                ans++;
        }
    }

    return ans;
}