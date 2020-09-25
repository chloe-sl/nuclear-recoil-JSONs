This repository presents a functional, standardized way to store nuclear recoil experimental data in a JSON format.

# What variables are currently represented by the JSONs?

name: The name or title of the experiment	(provided as a string)

identification:	A way to identify the experiment (archive number, etc)	(string)

field:	Strength of the electric field used in the experiment, in V/cm	(number)

yield_type:	‘charge’ or ‘light’	(string)

recoil_energy:	Recoil energy, in keVr	(number)

yield:	Yield values, in e-/keVr (if yield_type is charge) or ph/keVr (if yield_type is light)	(Number)

recoil_error:	Mean error for the recoil energy measurement (if max_recoil and min_recoil are included, recoil_error should be the mean of their values)	(Number)

max_recoil:	Difference between the maximum possible value of the recoil energy measurement and the given value (number)

min_recoil:	Difference between the minimum possible value for the recoil energy measurement and the given value	(Number)

max_yield:	Difference between the maximum possible value of the yield measurement and the given value	(Number)

min_yield:	Difference between the minimum possible value of the yield measurement and the given value	(number)

drift_field_error:	Uncertainty in the drift field, in V/cm	(Number)

gas_drift_field:	Drift field of the gas region, in V/cm (Number)

liquid_drift_field:	Drift field in the liquid, in V/cm	(Number)

extraction_efficiency:	Extraction efficiency assumed in the text	(Number)

pixey:	Extraction efficiency as predicted by PIXeY experiment	(Number)

corrected_energy:	Corrected recoil energy values (may be the same as recoil_energy)	(Number)
