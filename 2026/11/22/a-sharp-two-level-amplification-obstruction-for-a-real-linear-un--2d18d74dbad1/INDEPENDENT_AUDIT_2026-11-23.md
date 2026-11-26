# Independent mathematical audit

## correctness

PASS

For a first row (a,b), the image satisfies QQ*= (|a|²+|b|²)I and det Q=|a|²+|b|². Thus the map fixes I, sends U(2) to SU(2), and has norm one by row compression. With tensor factors switched, the output rows are P=[A B] and R=[−conj(B) conj(A)]; RR*=conj(PP*) gives ||R||=||P||≤||X||, and the squared output norm on a vector is at most twice ||X||² times the squared vector norm. For the displayed real J, J*=-J and J²=-I. These imply WW*=2I and Z=Z*, Z²=2Z; Z is nonzero. The switched entrywise image of W/√2 is exactly Z/√2, yielding equality on a unitary at k=2. Padding the two tensor sectors by identities preserves both the unitary input and the attaining output summand at every k>2. The non-Jordan check on E12 and E21 is valid. All computations are exact and concern the specified real-linear entrywise maps in the ordinary complex operator norm. The inspected CHECK.py is only supplementary, and was not executed.

## originality

PASS

Pass is for the exact amplification norms and unitary attainment, not the ordinary norm, quaternionic range, or classification of unital real-linear unitary preservers. No inspected independent result gives the quantitative assertion or a theorem that specializes to it without a separate sharpness computation.

## value

PASS

An exact matricial invariant of a natural exceptional map from a real-linear preserver classification is relevant to distinguishing scalar unitary preservation from its stronger matricial version. It locates the first obstruction and shows the largest distortion can actually occur on a unitary, rather than merely some matrix in the norm ball. The simple proof does not reduce this to the known scalar norm or to the qualitative non-Jordan observation; no broader classification or complex-linear completely bounded conclusion is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
