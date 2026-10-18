# Independent mathematical audit

## correctness

PASS

Set A_B=sum_{i in B}(d_i-2)>0. The existing published bound is U(B)=2^(|B|-1)(A_B+2), also valid for singletons where U({i})=d_i. For disjoint blocks I,J of sizes r,s, direct expansion gives U(I)U(J)-U(I∪J)=2^(r+s-2)[(A_I+2)(A_J+2)-2(A_I+A_J+2)]=2^(r+s-2)A_I A_J>0. Iterating merges proves every partition case. Sample integer arithmetic independently checked; the expansion itself proves universal strictness.

## originality

FAIL

The purported improvement is a mechanical one-line factorization of Canino–Casarotti–Santarsiero’s published all-factor formula U(B)=2^(|B|-1)(sum_{i in B}(d_i-2)+2): the gap equals 2^(r+s-2) A_I A_J. The source Theorem 1.1 already permits applying the direct bound to any union of blocks; repeated substitution yields all proposed comparisons without any new tensor analysis. The result is not independently original merely because the numerical inequality is not typeset verbatim in the source.

## value

FAIL

Although mathematically correct, the whole proposed theorem is a routine single-step factoring exercise on the exact all-factor formula already published. The partition comparison changes no rank bound, supplies no new decomposition, solves no independent sharpness question and cannot be viewed as a substantive structural lemma. Its verbal reframing as direct-versus-block composition does not rescue intrinsically mechanical content.

The dated certificate retains the supplied scientific assessment, sources and limitations.
