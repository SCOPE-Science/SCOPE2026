# Independent mathematical audit

## correctness

PASS

This PASS refers to the corrected finding, not the original decimal 0.77455285319149403… . Enumerating the nine ordered two-draw outcomes by applying half-averages to coordinate variables and taking the Hessian of the expected squared norm independently gives the stated restricted blocks and the reflection remainder d^2 C. For 0<b<1, the top eigenvector in the odd block has entries alpha>beta>0 and quadratic form (alpha-beta)^2/2 against C; hence every asymmetric law is strictly worse. Boundary laws without a connected support preserve a mean-zero vector. At an interior stationary point the top vector supports a quadratic with strictly positive second derivative and zero first derivative, so that point strictly beats every other b. The repaired proof makes the isolation exact: on [0.39,0.4], Q'>0 and 7-10b>0, and F' has the sign of Q'^2-4(7-10b)^2 Q=16P, whose signs at the endpoints are negative and positive. The independent algebra and numerical replay gives b*=0.3943218483533837932040… and F(b*)=0.7745528531914939319452… . The one-round odd block dominates the even eigenvalue for 0<b<1, G' vanishes only at 2/5, and the antisymmetric probability perturbation maps its unequal-coefficient top vector nontrivially into the even sector, excluding equality. For P3 the reflected remainder has eigenvalues 3/8 and 9/8 on disagreement, and the one-round factor is uniquely minimized by the maximal p1*p2; P2 has a single edge. Repaired RESULT.md and verify.py give corrected digits, an exact signed sextic check and the correct number of two-draw outcomes. Frozen support was read, not run; the independent Hessian, exact sign and numerical replay is /tmp/opencode/frozen-review-replay.py (gossip). The result does not concern adaptive choice, different laws in the two rounds, or another horizon.

## originality

PASS

The corrected claim is the exact, unique minimax horizon-two optimizer, its strict separation from the one-round law, and path minimality under the stated iid protocol. The self-match is not evidence of a separate result; the strongest distinctly indexed exact horizon-two results concern isotropic input, and the inspected classical sources optimize a one-round eigenvalue or study long-run convergence. None of that coverage supplies the claimed deterministic worst-input optimizer. The repairs leave the objective, exact optimizer and minimality unchanged.

## value

PASS

The absolute gain is only about 3.7751e-5, but the exact gain matters as a strict counterexample to a natural and widely usable one-round spectral design surrogate. The result identifies the first path where two iid minimax rounds require another law, supplies both unique designs and excludes every possible asymmetric improvement; neither a numerical optimization nor an isotropic average would settle that question. No practical speedup claim is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
