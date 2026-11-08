# Scientific review

## Correctness

**PASS.** The claim is restricted to the exact map and geometric inducing scheme of Ji–Ma at \(\lambda=1/2\), initialized uniformly on a single specified level-five branch. The cited branch-image and roof identities are directly present in [1], and their affine restriction transfers the level process to a skip-free walk with i.i.d. geometric increments. The first-passage generating function \(U(z)=1-\sqrt{1-z}\) and its Catalan coefficients follow algebraically. Optional stopping at the first zero/upper-barrier crossing is justified by a geometric upper bound on the stopping time and integrable overshoots, and yields exact \(1/(h+1)\) heights. Fibonacci roof growth and the Catalan tail give the two-sided bound leading to \(\log\varphi/\log T\). An independently executable finite checker supports, but does not prove, those infinite assertions.

## Originality

**PASS within accessible evidence.** Ji–Ma [1] prove qualitative critical null recurrence and use the same induced level process; the new statement is neither a new claim of criticality nor an alternate proof of that result. The exact original-time accumulated roof-excursion tail, including the sharp golden-ratio coefficient, does not appear in the inspected formulas or conclusions of [1]. Bruin–Todd [2,3] concern related unimodal/infinitely branched models and thermodynamic quantities, not the defined bimodal original-clock stopping variable. Ma [4] studies a smooth cubic family. Closest indexed analogues concern different dynamical systems or Fibonacci combinatorics with different observables. Absence of a match is not a uniqueness proof; a general result for critical skip-free renewal walks with exponential roofs might imply the statement and remains the principal risk.

## Mathematical value

**PASS.** A sharp quantitative recurrence invariant is natural at the precise parameter where the originating family becomes null recurrent. The same excursion has a polynomial tail in *inducing steps* but an inverse-logarithmic tail in *original map iterations*, with all positive original-clock moments infinite. The conversion is not obtained from the drift test of the original paper: it uses the full maximum-height law, a memoryless overshoot correction, and the Fibonacci growth of return times. This distinction is relevant for original-time ergodic observables and return statistics, without asserting an unproved mixing-rate consequence.

## Closest literature and limitations

The four inspected works are Ji–Ma (2023), Bruin–Todd's 2011/2019 infinitely branched map article, Bruin–Todd's Fibonacci unimodal wild-attractor article, and Ma's 2024 smooth cubic article, with references and material specifics in RESULT.md and AUDIT.json. The original-clock variable ends an inducing block and need not equal the first ordinary-iterate visit to the stopping set. The special critical parameter and the specified initial distribution are integral to the theorem; no universality or independent priority certification is claimed.

Self-review: passed. Independent audit: not yet performed.
