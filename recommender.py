def generate_recommendation(
        avg_score,
        avg_confidence):

    prediction = round(
        (avg_score*0.65)
        +(avg_confidence*0.35),
        2
    )

    if prediction >= 88:

        readiness="HIGH"

        advice="""
Ready for advanced technical interviews.
Focus on leadership,
system architecture,
behavioral excellence.
"""

    elif prediction >=75:

        readiness="MEDIUM"

        advice="""
Good performance detected.
Improve weak categories,
mock practice,
confidence refinement.
"""

    else:

        readiness="LOW"

        advice="""
Further preparation recommended.
Strengthen fundamentals,
communication,
problem solving.
"""

    return{
        "readiness":readiness,
        "prediction":prediction,
        "recommendation":advice
    }