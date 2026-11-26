# Independent mathematical audit

## correctness

PASS

Trace the product by summing cyclic 0/1 labels: A_s(x_{j-1},x_j) is zero for adjacent ones and otherwise gives s if x_j=1 and 1 if x_j=0. Over F2 both matrices have projective transfer period three, with odd trace off lengths divisible by three. For a trace-zero product at such a multiple, M=I+2B and tr B=-1 imply det M=-1 mod 4, hence det M=-1 rather than +1. Cayley–Hamilton gives a nontrivial projective involution. With R=A_- and T=A_+R^{-1}, direct multiplication gives R^3=-I and T^2=I. The stated intervals work: R and R^2 send V into U and T sends U into V. A cyclically reduced alternating word can be rotated to start with T and end with R^a; conjugation by R^b with b nonzero and b different from a gives a reduced word with R syllables at both ends, taking V into U. This proves faithfulness along with the evident nonidentity single-factor syllables. A finite-order projective word therefore cyclically reduces to one factor; the involution type is T. With p odd plus signs, write it cyclically as p copies of T separated by positive R-gaps. For p=1 the gap is a positive multiple of three. For p>=3 a multiple-of-three gap must exist or the word is cyclically reduced of infinite order. Trim three from a gap of at least six, or cancel TR^3T at a length-three gap and concatenate its neighboring gaps. This preserves the torsion type and yields n>=3(p+1)/2 by induction. Thus |S|>=k+1 at n=3k. The trace of +-- is zero and A_+A_-^2A_+=-A_- increases length by three and minus weight by one, proving attainment at every k. Character diagonalization is for the full Boolean group with the unnormalized indicator; n=3 is a simple triangle as required. Both frozen verifiers and recorded evidence were inspected, not executed. Direct parity-intersection summation over independently generated cycle sets (python3 /workspace/review_checks.py 2) gives first weights 2,3,4,5 at n=3,6,9,12 and no zeros at other n through 14. The universal proof does not rely on these bounds.

## originality

PASS

The all-length first-zero weight, not the known modulo-three invertibility boundary, is the supported distinct claim. The earlier low-degree classification overlaps and implies the first two singular cases; it does not settle the growing threshold at n>=9 in the material compared. The unrestricted cyclic transfer formula is prior machinery, not the new claim.

## value

PASS

The first zero is exactly the lowest degree at which a Walsh component can be lost in cyclic hard-core convolution. Sharp all-length injectivity and explicit witnesses clarify the singular regime beyond both mod-three invertibility and bounded-degree lists. The free-product reduction provides a structural reason for the linear threshold. This is noiseless injectivity, not a bound on noise amplification or a full nullity classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
