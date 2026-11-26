# Independent mathematical audit

## correctness

PASS

Cubing numbers modulo three leaves them unchanged, so f_n reduces to (−1)^n. For B=3^L, Lucas on B−1 gives the exact interior binomial valuation L−v_3(j). Cubing implies f_B≡2 mod 27, which makes f_B have order 2·3^{k−1} modulo 3^k. At precision 3^k and q=3^{L−k+1}, a Vandermonde summand can survive only if its high-block index is a multiple of q; a<q forces the low summand index to equal the target index mod q. Cubing and summing gives the separated product including endpoints. Repetition of one generator in infinitely many spaced positions, using between 1 and h=2·3^{k−1} of them, gives every unit with a positive sparse ternary witness and arbitrarily large witnesses. Among h(h−1)+1 positions one residue occurs at least h times, proving the bound. The closure and measure follow from coverage at every precision and exclusion of nonunits. An independent modular-Pascal replay verified 4,908 block identities through k=7 and full unit coverage through modulus 243, with incomplete coverage at 729 and 2187 in the finite sample of indices below 6561. This incompleteness does not contradict the all-index theorem.

## originality

FAIL

The all-level sparse-witness statement is mechanically implied by the previously published Dwork quotient congruence specialized to the Laurent constant-term expression for Franel numbers. This is stronger evidence than the existence of p-automata or isolated digit congruences. The implication below even gives a smaller witness bound. No identical printed statement was found in the inspected sources.

## value

FAIL

All-level value images and sparse witnesses are natural questions, and the submitted proof is compact. But for this sequence the exact conclusions are elementary consequences of a previously available uniform congruence, including a stronger explicit bound by the same argument. The checked result does not add an independent invariant or a stronger witness conclusion beyond that readout of prior results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
