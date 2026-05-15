def EuclidAlg(a, b):
    '''
    Finds the integer greatest common divisor of two integers.

    Parameters
    ----------
    a : integer
    b : integer

    Returns
    -------
    GCD of a and b as a positive integer.

    Example
    -------
    gcd(196, 72)
        -> 4
    '''
    
    
    if b > a:
        a, b = b, a
    
    if a == b:
        return a
    elif (a % b) == 0:
        return b
    elif a == 0: 
        return b
    elif b == 0:
        return a

    keepCalculating = True
    while keepCalculating:
        r = a % b
        keepCalculating = ((b % r) != 0)
        a = b
        b = r
    if r > 0:
        return r
    if r < 0:
        return abs(r)
    
# crystallography
def LatticePeriod(period1, period2):
    '''
    Finds the smallest repeating subpattern in a crystal
    with respect to two directions.

    Parameters
    ----------
    period1 : integer
        repetition period (lattice units) in crystal pattern 
        with respect to an specific direction.
    period2 : integer
        repetition period (lattice units) in crystal pattern 
        with respect to a different specific direction.

    Returns
    -------
    Smallest repeating subpattern in crystal with respect
    to both directions.

    Example
    -------
    LatticePeriod(24, 36)
        -> 12
        Both directions share a fundamental periodic block
        every 12 lattice units.
    '''

    
    return EuclidAlg(period1, period2)


def Supercell(materialA, materialB):
    '''
    Finds the contents of a supercell within a superlattice
    composed of two repeatedly stacked materials.

    Parameters
    ----------
    materialA : integer
        repetition period of material A in lattice units. 
    materialB: integer
        repetition period of material B in lattice units.

    Returns
    -------
    3 float values corresponding to the integer number of 
    lattice spacings, the number of repetitions of material A,
    and the number of repetitions of material B.
    
    Example
    -------
    Supercell(8, 12)
        -> 24, 3, 2
    '''


    a = EuclidAlg(materialA, materialB)
    b = (materialA * materialB) / a  # LCM
    c = b / materialA
    d = b / materialB
    
    return b, c, d

# common periods in oscillations
def OscillationSync(period1, period2):
    '''
    Finds the common synchronization period of two oscillators.

    Parameters
    ----------
    period1 : integer
        Oscillation period of oscillator 1. 
    period2 : integer
        Oscillation period of oscillator 2.

    Returns
    -------
    Common synchonization period of oscillators 1 & 2, in time 
    units.

    Example
    -------
    OscillationSync(12, 18)
        -> 36
        Oscillators 1 & 2 sync every 36 time units.
    '''

    
    a = EuclidAlg(period1, period2)
    b = (period1 * period2) / a  # LCM
    return b

# wave interference/resonance
def FundamentalSharedFreq(freq1, freq2):
    '''
    Finds the fundamental shared frequency of two frequencies.

    Parameters
    ----------
    freq1: integer
        Frequency 1 in Hz.
    freq2: integer
        Frequency 2 in Hz.

    Returns
    -------
    The fundamental shared frequency of which freq1 and freq2
    are harmonics, in Hz.

    Example
    -------
    FundamentalSharedFreq(480, 360)
        -> 120
    '''

    
    return EuclidAlg(freq1, freq2)