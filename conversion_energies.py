import numpy as np

SUP_FLUX_QUANTUM = 2.067833831e-15 # kg⋅m^2⋅s^−2⋅A^−1
E = 1.6021766208e-19 # C (A·s)

def calculate_Ej( Jc, A ):
    """
    Calculates Josephson Energy

    Parameters:
    Jc (float): Josephson critical current density (uA·um^-2)
    A (float): Junction Area (um^2)

    Returns:
    Ej(float): Josephson energy(GHz)

    """
    Jc = convert_uA_over_um2_to_A_over_m2(Jc)
    A = convert_um2_to_m2(A)

    Ic = Jc * A
    Ej = Ic * SUP_FLUX_QUANTUM / (2*np.pi)

    Ej = convert_J_to_GHz(Ej)
    return Ej

def calculate_Ec( C ):
    """
    Calculates Charging Energy

    Parameters:
    C (float): Capacitance (fF)

    Returns:
    Ec(float): Charging energy(GHz)

    """
    C = convert_fF_to_F(C)
    Ec = E**2/(2*C)
    Ec = convert_J_to_GHz(Ec)
    return Ec

def convert_uA_over_um2_to_A_over_m2(value):
    """
    Converts value in units uA/um^2 to A/m^2
    """
    value *= 1e6
    return value

def convert_um2_to_m2(value):
    """
    Converts value in units um^2 to m^2
    """
    value *= 1e-12
    return value

def convert_J_to_GHz(value):
    """
    Converts value in units J to GHz
    """
    value *= 1.509190311676e+24
    return value

def convert_fF_to_F(value):
    """
    Converts value in units fF to F(s^4⋅A^2⋅m^−2⋅kg^−1)
    """
    value *= 1e-15
    return value

def calculate_C( Ec ):
    """
    Calculates capacitance from charging energy

    Parameters:
    Ec (float): capacitive energy (GHz)

    Returns:
    C(float): Capacitance (fF)
    """
    Ec = convert_GHz_to_J(Ec)
    C = E**2/(2*Ec)
    C = convert_F_to_fF(C)
    return C

def convert_GHz_to_J(value):
    """
    Converts value in units GHz to J
    """
    value /= 1.509190311676e+24
    return value

def convert_F_to_fF(value):
    """
    Converts value in units F(s^4⋅A^2⋅m^−2⋅kg^−1) to fF
    """
    value *= 1e15
    return value