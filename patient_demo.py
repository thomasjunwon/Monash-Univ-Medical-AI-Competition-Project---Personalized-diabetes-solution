DEMO_FEATURES = {
    # demo (숫자 인코딩)
    "gender": 1,      # Male
    "race": 3,        # White
    "marry": 1,       # Married/Living with partner
    "age": 52,
    "educ": 4,        # Some college / AA degree
    "house": 3,
    "pov": 1.7,

    # anthropometrics
    "wt": 88.5,
    "ht": 173.0,
    "bmi": 29.6,
    "wst": 102.0,
    "hip": 100.0,

    # vital
    "sys": 138.0,
    "dia": 86.0,
    "pulse": 78.0,

    # liver
    "alt": 42.0,
    "albumin": 4.2,
    "ast": 36.0,
    "ggt": 65.0,

    # renal
    "crea": 1.0,
    "acratio": 22.0,

    # metabolic
    "chol": 212.0,
    "ldl": 138.0,
    "hdl": 41.0,
    "tyg": 8.8,
    "glu": 108.0,
    "insulin": 15.0,

    # inflam
    "crp": 3.8,
    "wbc": 7.2,

    # cbc
    "hb": 14.6,
    "hct": 43.0,

    # lifestyle (summary)
    "mvpa": 70.0,
    "ac_week": 8.0,
    "veg_week": 5.0,       # 4–6 meals/week의 대표값
    "sleep_avg": 5.5,      # 5–6h/night
    "bedtime_score": 3,    # 11 pm–12 am

    # extra
    "h3a1c": 5.9,

    # context
    "context": (
        "Patient works as a mid-level office manager and reports late meetings "
        "and frequent evening work emails. Meals are often restaurant-based due "
        "to convenience. Lives with spouse and one teenage child. Reports "
        "moderate work-related stress and inconsistent sleep schedule with "
        "regular screen exposure before bed. States: “I know I should do better, "
        "I just can’t stick to it.” No financial barriers but low motivation for "
        "lifestyle change."
    ),
}