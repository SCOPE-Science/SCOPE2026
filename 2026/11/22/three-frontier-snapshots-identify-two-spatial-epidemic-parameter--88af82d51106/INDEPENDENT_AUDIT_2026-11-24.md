# Independent mathematical audit

## correctness

PASS

With C=R+R_infinity Q, the clearance terms cancel exactly, giving dC/dt=gamma I. Dividing by dP/dt, which is strictly negative under the hypotheses, and integrating gives the two recovery increments with the same multiplier gamma*pi/(2*rho) on the arctangent integrals. For the weight 1/arctan(ku), its k log derivative is -eta(ku)/k. The derivative numerator of eta is (1-z^2) arctan(z)-z, negative for z>=1 and also for 0<z<1 since arctan(z)<z. The weighted mean of eta on the lower interval strictly exceeds its mean on the upper; the ratio is therefore strictly increasing. Uniform small- and large-k limits on the positive compact population interval give precisely L and U. The ratio has range (L,U), and a unique k there yields a unique rho by either increment and a unique alpha for known N. The supplied checker was inspected, not executed; quadrature, finite differences and the RK4 illustration are not the proof. The converse and sharpness are for the reduced relation, not feasibility in the full system. For unknown N or gamma, the direct invariants are alpha/N and rho/gamma; the last section's 'only rho/gamma' should not be read as ruling out identification of alpha/N.

## originality

PASS

The model and saturation are prior work. The supported distinct contribution is the exact sharp range and injectivity of this finite-snapshot ratio, not a new model, a full-trajectory inverse or a general structural-identifiability method.

## value

PASS

The two-interval ratio gives an exact falsification criterion and the minimum number of observations for this reduced inverse relation: one interval leaves a continuum of fits, whereas two identify both dimensionless combinations. It removes clocks and nuisance dynamics from this specific model comparison. The result is mathematically useful without promising stable estimation, epidemic forecast accuracy, or full-model feasibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
