# Independent mathematical audit

## correctness

PASS

There are 20 lines, 480 bases, 90 bases through a point and 12 through a pair. Expanding (1-2) to the intersection size yields W(S)=480-180k+48 binom(k,2)-8 binom(k,3)+8t, where t counts the collinear triples in S. For k<5 the part independent of t is positive, and at k=5 it is not divisible by 8. At k=6 cancellation needs t=5; without a full line, five collinear triples would partition the pairs of six points into triangles, impossible at odd vertex degree. With a full line the only extra collinear triple uses the two exterior points and the intersection of their joining line with the full line. This gives 20 times (66-18)=960. The independent field/coset replay matched the entire absolute Walsh table and complement-sign relation, the zero counts (960,4230,960) at weights (6,8,10), the rank 59386, and the projection-support transform numerator 2232436. Largest and least nonzero magnitudes are 480 and 4, so the nonzero-spectrum condition number is 120. Translation-averaging any projection preserves identity on the prescribed range, keeps the image in that range, and cannot increase its endpoint norm. The unique commuting projection is the support multiplier, with both endpoint norms equal to the absolute kernel sum (real or complex), giving exactly 558109/16384. Replay: /workspace/branches/93fb65a0-4dc7-420f-b86c-2cec86339a46/replay_record2.py and replay_record2.log, with the supplied verify.py and reproducibility notes inspected but not executed.

## originality

PASS

Best of knowledge, the supported contribution is the exact first-cancellation geometry, full multiplier data, and the resulting exact endpoint projection constant for the GF(4) affine plane's basis-incidence convolution. The coefficient expansion and the norm-minimizing averaging technique are methods, not original claims. Closely related affine-plane computations at other parameters are credited separately from this case.

## value

PASS

AG(2,4) is a standard small affine plane with four-point lines; its natural basis-incidence operator tests cancellation outside the three-point-line Steiner setting. The nullity measures the precise obstruction to recovery, the minimal supports show that the first lost frequencies have a rigid geometric cause, and the sharp endpoint constants measure the unavoidable cost of projecting onto the recoverable modes even without imposing translation invariance. The full small-instance invariant is useful beyond an unsupported spectrum computation or a routine averaging lemma.

The dated certificate retains the supplied scientific assessment, sources and limitations.
