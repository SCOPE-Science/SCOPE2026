/*
www-ATLAS of Group Representations.
U4(2):2 represented as permutations on 27 points.
*/

G<x,y>:=PermutationGroup<27|\[
1,3,2,6,8,4,12,5,16,10,11,7,13,14,15,9,17,18,22,20,21,19,23,24,25,
26,27]
,\[
2,4,1,7,3,10,13,14,5,15,6,19,17,21,8,20,9,11,24,12,23,16,18,26,22,
27,25]
>;
print "Group G is U4(2):2 < Sym(27)";
