# Independent mathematical audit

## correctness

PASS

For b≥3, coefficients in residues 0 and 1 are p(u)+p(u−1), while other residues give p(u). For residue zero the previous index uses residue b−1 and quotient u−1, including the convention p(−1)=0. Thus the claimed adjacent-pair automaton, its leading-zero convention, and the absorbing 00 state check out. In the active-state counts, x−z=1 and x_(m+1)=A_m; summing the odd-output coordinates yields A_(m+2)=(b−2)A_(m+1)+4A_m−2 with 1,b initially. Its generating function and pole coefficient follow by summing the recurrence and using λ²=(b−2)λ+4. The positive root lies between 2 and b and exceeds the magnitude of the negative root; squeezing between consecutive powers proves the arbitrary-cutoff order and density zero. Independently for the smaller cap, the same state pair has transitions (v+w,w), (v,v+w), (v,v) for digits 0,1,others, respectively. The resulting affine recurrence has quadratic t²−(b−1)t−2. Evaluating the enlarged-cap quadratic at that positive root ρ gives ρ−2>0. Binary cap three splits each digit into independent bits at powers j and j+1, giving [(1−z)(1−z²)]^(−1) and odd residues 0,1 mod 4. An independent truncated GF(2) product using shifted bitsets agrees for bases 3–12, both caps, all levels through five, and binary cap three through level 12. Replay: python3 /workspace/reproductions/frozen_math_checks.py 4; output /workspace/reproductions/record-4.txt.

## originality

PASS

The distinct claim is the exact aggregate parity law at cap b+1 and its strict spectral comparison to cap b. The strongest exact source treats cap b, not b+1; the distinct same-day source is likewise cap b and gives a different modular counting theorem. Coons treats the same general representation function and establishes standard digit-regular machinery and coefficient asymptotics, but the inspected statements do not give the distribution of parity states for this cap or its exact spectrum. This is a bounded best-of-knowledge judgment, not a priority certificate.

## value

PASS

The first larger cap is a natural test of whether increasing the representation set preserves parity-support size. The exact full-level counts and distinct spectral exponents show a uniform strict reversal across all b≥3 despite pointwise nondecreasing representation counts. This quantifies how much sparser the odd support becomes, and provides the precise enumerator for either analytic or computational comparison, not just finite examples or automaticity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
