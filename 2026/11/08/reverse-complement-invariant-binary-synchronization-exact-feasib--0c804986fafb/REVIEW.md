# Independent mathematical audit

## correctness

PASS

The orbit {w,rho(w)} is non-overlapping exactly when w is unbordered and has no self-reverse-complementary proper prefix or suffix; this follows by enumerating both self and cross overlaps. The binary length-one overlap forces all nonempty codewords to share one start/end orientation. For lengths 3,5,7 the residual middle-bit candidates have an explicit forbidden even antipalindromic segment, while the length 1,2,4,6 witnesses and w_n=0^(n-5)11011 for all n>=8 pass the same criterion. The guard family 0^k1u01^k is rho-closed, has unique initial 0^k marker and no cross bifixes; the union bound yields at least 2^(n-2k-3)>2^n/(512n^2) for k=ceil(log2(4n)). Limits use n sufficiently large, not the small-length witness. Independent exhaustive small codeword-orbit checks support the proof.

## originality

PASS

Classical non-overlapping code constructions (Chee et al. 2012, Blackburn 2013) do not require closure under reversal and bitwise complement. Published small fixed-point-free complement-alphabet size spectra at length three do not establish the binary existence gap or the invariant full-rate construction. No searched published statement implies both the exceptional lengths and the binary rate.

## value

PASS

Preserving non-overlap under a natural involution is a structurally motivated synchronization-code constraint. The exact exceptional lengths 3,5,7 and existence of positive exponentially large symmetric code families resolve concrete feasibility and asymptotic-capacity questions, rather than only an arbitrary finite example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
