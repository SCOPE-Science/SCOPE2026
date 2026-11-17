# Independent mathematical audit

## correctness

PASS

For output leaf x at depth k, its signed Haar kernel is constant on each first-divergence sibling subtree, with mass 2^(-j-1), and on x with mass 2^(-k). The signed total variation reduces exactly to sum_{j<k}(1-sigma_j z_j)/2+|z_k|, where z_0=1 and z_{j+1}=(z_j+sigma_j)/2. The Bellman recursion V_m=a_m+c_m|z| has c_m=(1-c_{m-1})/2 and yields F_k. Thus all other branches cancel by mass conservation. Maximum row norm is F_H, attained by choosing the input sign of the kernel. F_{h+1}>F_h for h>=1, and full-binary leaf-count/height inequalities plus successive off-spine leaf splits realize every permissible h; H=N-1 forces a comb. The N=1,2 boundary and maximizing row signs are consistent. Independently enumerated all ordered proper binary trees with <=6 leaves: 65 trees and 351 leaf rows, checking the depth values and height sets. The finite check corroborates but does not prove the unrestricted statement.

## originality

PASS

The full homogeneous depth-H constant and optimal sign path are EXACTLY in an earlier separate result; they are prior art. However that publication expressly excludes incomplete subtrees and the assertion that arbitrary branch pruning leaves each row norm unchanged. The tree-height spectrum and comb versus shallow extremizers are additional necessary mathematical deductions, not contained in the complete-level statement. No searched source entailed pruning invariance; status PASS best-of-knowledge for that nontrivial extension only.

## value

PASS

An adaptive dyadic partition has a naturally variable number and depth of leaves; determining its exact sharp endpoint amplification from height alone, and the entire possible list at fixed dimension N, is a useful structural classification and quantitative comparison of extremely unbalanced to balanced trees, not merely another evaluation of the known complete dyadic constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
