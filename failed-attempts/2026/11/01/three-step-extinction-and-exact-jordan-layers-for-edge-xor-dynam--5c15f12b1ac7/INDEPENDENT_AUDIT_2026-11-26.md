# Independent mathematical audit

## correctness

PASS

The open-neighbor rule is C^t C for the unoriented incidence C, since its diagonal is two and hence vanishes. The image of C is the augmentation hyperplane W and the kernel of C^t is the line of constants inside W; this gives rank 2^d-2. Independently split the cube along its last bit: with S the sum of I+flip_i over the remaining bits, B=I+S satisfies B^2=I and preserves augmentation and constants. Then CC^t has block matrix [[B,I],[I,B]], squares to zero, and sends (a,b) to (x,Bx) with x=Ba+b. For inputs in W the attainable x are exactly the vectors of augmentation zero on the half-cube. The full constant vector belongs to this image because the half-cube has even order for d>=2. Thus rank(C^t(CC^t)C)=2^(d-1)-2, and the third power vanishes. The rank differences give the stated Jordan blocks and kernel-dimension differences give the labeled populations, including the index-two square and sharp index three thereafter.

## originality

FAIL

A distinct October 26 Resultary record proves the exact binary rank sequence, nilpotence, Jordan partition and cumulative populations. Each update matrix and all its powers are scalar extensions from F_2, so their ranks are unchanged; the field-size census then follows from the order of a vector space. The extension to all finite characteristic-two fields is mechanically implied, not a surviving distinct claim.

## value

FAIL

The exact structural binary classification would be useful for a natural parity automaton, but the only extra stated scope is a scalar extension of that classification and conversion of kernel dimensions to finite-field cardinalities. It supplies no independent new structural information or motivated new invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
