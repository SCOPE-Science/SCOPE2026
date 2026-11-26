# Independent mathematical audit

## correctness

PASS

Conditioning on the frozen arrows leaves two independent uniform targets. An arrow into the sink basin closes exactly one cycle and an arrow outside closes none. A single inside target gives either sign with equal weight k(n−k)/n²; it is uniform in the rooted tree, yielding the path mark. Cayley counting with the specified basin vertex set gives b(n,k), with K=n having mass 1/n and only a zero jump. Rooted forest extension of a prescribed depth-h path gives a(k,h)=(h+1)(k−1)_h/k^(h+1). This equals t_h−t_(h+1) for t_h=(k−1)_h/k^h, so its tail at h≈r√k tends to exp(−r²/2). The one-sign basin weight is (n−k)/n² times the binomial mass at k for success probability k/n. Stirling gives its interior density at scale n^(−3/2), with uniform envelope proportional to u^(−1/2)(1−u)^(1/2), whose endpoint contributions vanish as the truncation is removed. Its integral with the normalizing factor 1/√(2π) is √(π/8), giving the beta mark and the total rate. The conditional basin size tends to infinity in probability; the depth kernel then yields independent Rayleigh after division by √K, and multiplication by √(K/n) gives the asserted joint mark. Independently enumerated n=3 masses per sign are 8/81, 2/81, 2/81 at (1,1), (2,1), (2,2) (branches/e546cb88-f6d2-4a5d-96ef-cc3b4006ef5a/independent_n3.py and independent_n3.txt). Frozen verify.py was inspected, not executed.

## originality

PASS

The root-inclusive static basin marginal and rooted Cayley height law are not new. The supported distinct claim concerns the one-arrow before/after jump, including its limiting intensity and the joint basin and cycle-length marks under jump conditioning.

## value

PASS

The result identifies both how often a single-coordinate update changes the component count and the length distribution of the affected cycle on that rare event. The basin and length marks specify the jump geometry that an unmarked probability or a preserved-cycle count would miss.

The dated certificate retains the supplied scientific assessment, sources and limitations.
