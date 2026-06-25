/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
void inorder(struct TreeNode* root, int* ans, int* returnSize) {
    if(root==NULL){
        return;
    }
    inorder(root->left,ans,returnSize);
    ans[(*returnSize)++]=root->val;
    inorder(root->right,ans,returnSize);

}
int* inorderTraversal(struct TreeNode* root, int* returnSize) {
    int* ans = (int*)malloc(100 * sizeof(int));
    *returnSize=0;
    inorder(root,ans,returnSize);
    return ans;
}