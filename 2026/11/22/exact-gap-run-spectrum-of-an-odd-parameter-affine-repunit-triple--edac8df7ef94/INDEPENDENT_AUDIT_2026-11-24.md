# Independent mathematical audit

## correctness

PASS

For t=y+3z the least coefficient of a is C(t)=2(t−floor(t/3)), attained at z=floor(t/3). Odd a makes 2t invertible modulo a; C is nondecreasing, so the least nonnegative t for each residue gives its Apéry minimum. For a=2m+1 the even thresholds are C(j) and the odd thresholds C(m+j+1)+1. Consequently the even members form a prefix of each row and any represented odd residue has both adjacent evens represented. The only nonsingleton run in a row is its terminal interval, bounded on the right by the next multiple of a. A terminal length 2(m−j) occurs C(j+1)−C(j) times, giving the asserted 0-or-2 law. Subtracting the terminal lengths from the summed thresholds gives B1=2m²+m−2(F(2m)−2F(m)), with F(N)=sum_{t=1}^N floor(t/3); its three evaluations agree. The redundant-generator boundary a=3 has B1=3 and B2=2. An independent reachability census matched all 50 odd a=3..101, stopping at a consecutive members to certify the entire tail. Replay: /workspace/branches/7467a3e0-effd-4bb7-9a5e-c37cb588a06d/local_reproduction.py. The frozen checker was inspected, not run; finite agreement supports but does not prove the general identities.

## originality

PASS

The supported distinction is the complete ordinary gap-run histogram of the increment-two triple, not the semigroup family, Apéry method, or its genus. Known exact membership data do not by themselves give the adjacency reduction or its period-three counts. No inspected result states or directly subsumes the histogram; this is a best-of-knowledge judgment.

## value

PASS

The triple is a natural short affine-repunit family. A full census distinguishes isolated gaps from the paired terminal runs, identifies missing lengths by a congruence condition, and supplies exact frequencies without enumerating all gaps. Neither the genus nor the presentation describes that local geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
