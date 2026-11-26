# Independent mathematical audit

## correctness

PASS

Greedy minimal complete-alphabet blocks compute the index: their completion letters followed by a letter missing from the remainder give a nonembedded target. In a proper word with j letters seen, j−1 legal repeats and q−j acquisitions give the stage products. The first position contributes q rather than q−1 choices, including the correct separate empty word. Under uniform legal transitions, the acquisition hazards depend only on j, so strong Markov restart gives independent geometric delays and independent arch lengths. This yields the stated moments, the CLT for q≥3 and the ternary binomial survival law; for q=2 the length is deterministically two. For the bounded moment errors, it is 1−φ that has a simple zero at 1: the differentiated renewal series have poles of orders two and three. With s=1−z and a=E[L(L−1)]/2, the first moment series starts μ⁻¹s⁻²+(a/μ²−1)s⁻¹, and the second factorial moment series starts 2μ⁻²s⁻³+(4a/μ³−4/μ)s⁻². Coefficient extraction and centering give (2a+μ−μ²)n/μ³+O(1); span one and exponential moments isolate the dominant singularity. At length qk all arches are permutations and each later first letter must avoid the last letter of the previous arch. Independent finite check: generate every proper host for q=2,3,4,5 with n≤8,10,8,5 respectively; test all targets up to floor(n/q) by a forward subsequence scan. This counted 17,914 hosts, 157,505 pattern tests and matched all 15 nontrivial ternary survival cases tested. At q=3,n=9 the exact-index counts were (6,138,528,96), and at q=4,n=8 they were (1524,6792,432). The frozen verify.py is an additional documented replay path, inspected but not executed; finite checks do not establish the asymptotics.

## originality

FAIL

A distinct indexed result gives the same proper-host model, full all-q distribution, ternary rational law, renewal constants and Gaussian law, and shortest-host enumeration. This is a failure to establish a distinct mathematical finding against existing coverage, not a finding of who derived it first. The mirror path date is later than the frozen record date, and neither the relationship nor priority is established. The binomial-tail phrasing absent from the mirror follows by summing its exact distribution (or by expanding the kth power of its ternary arch generating function); it does not supply a distinct remainder.

## value

PASS

As mathematics, this is a useful exact solution for a natural regular host language: it replaces generic automata counting with a uniform closed form and a tractable probabilistic law for a canonical constrained-word model. That value does not imply distinctness, and the elementary ternary-tail rewrite alone would not rescue the covered contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
