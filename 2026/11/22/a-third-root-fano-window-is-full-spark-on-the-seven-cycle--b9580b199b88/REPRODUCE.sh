#!/bin/sh
set -eu
cd "$(dirname "$0")"
CC=${CC:-cc}
${CC} -O3 -std=c11 ternary_full_spark.c -o /tmp/ternary_full_spark_check
/tmp/ternary_full_spark_check
${CC} -O3 -std=c11 independent_ternary_check.c -o /tmp/ternary_full_spark_independent
/tmp/ternary_full_spark_independent
${CC} -O3 -std=c11 binary_certificates.c -o /tmp/binary_gabor_certificate_check
/tmp/binary_gabor_certificate_check | cmp - binary_witnesses.csv
python3 direct_integer_checks.py
