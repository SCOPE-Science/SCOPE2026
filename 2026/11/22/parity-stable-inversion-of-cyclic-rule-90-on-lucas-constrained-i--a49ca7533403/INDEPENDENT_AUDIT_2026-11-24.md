# Independent mathematical audit

## correctness

PASS

For the repaired theorem, multiplication by z^-1(z+1)^2 models the cyclic update, including two coincident neighbors at n=2. If n=2^s u with u odd, the multiplicity of z+1 in z^n-1 is 2^s; the kernel of multiplication by a polynomial f in the quotient is the space of multiples of (z^n-1)/gcd(f,z^n-1). Thus the nested kernels have dimensions min(2t,2^s) starting at t=0. For odd n the only nontrivial difference at positive time is the all-one complement mask, excluded by odd cyclic length and the simultaneous absence of 11 and 00. For even n set M=2^s. For every 1<=t<=M/2, the exponent M-2t is even, so (z+1)^(M-2t) encodes a length-M word supported on even indices and repeated admissibly to obtain length n. Repetition intertwines the updates and is injective. Modulo (z+1)^M, the image of that word at t-1 is a unit shift of (z+1)^(M-2), nonzero, and at t is zero. This finds an actual collision of two different time-(t-1) outputs at each stated step, including n=2. Thereafter the ambient kernels and hence the actual source partitions agree. Counts of images, not equality of the sets of images, stabilize. Ran the newly written CHECK.py in the corrected files: VERIFY_OK n=2..16: image counts and all strict-step witnesses.

## originality

PASS

The repaired contribution is the exact time horizon of strict losses on the constrained source, with an admissible witness at every increasing kernel stage. The all-state kernel and one-step constrained inverse-fiber census are credited, not reasserted as novel results. The exact constrained horizon is not covered in the inspected stronger and equivalent formulations.

## value

PASS

The indexing, hard-core language and synchronous dynamics are canonical. A nonlinear source restriction can hide ambient rank losses, so knowing the all-state horizon does not answer whether observation precision continues to degrade on this source. The theorem proves that no growing-kernel stage is hidden at even lengths, identifies exactly when a decoder's source partition will stop changing, and gives explicit admissible collision witnesses at every step up to that boundary. This is a natural time invariant and an exact structural guarantee, not a repeat of the one-step count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
