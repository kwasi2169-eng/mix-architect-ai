import time

def gain_staging_agent(question):
    return f"""You are a Gain Staging Architect.
Focus only on: Headroom, Clipping prevention, Gain structure, Pre-master levels.
Question: {question}"""

def depth_agent(question):
    return f"""You are a Depth Architect.
Focus only on: Front-to-back placement, Reverb strategy, Spatial design.
Question: {question}"""

def focus_agent(question):
    return f"""You are a Focus Architect.
Focus only on: Listener attention, Instrument hierarchy, Chorus impact.
Question: {question}"""

def release_readiness_agent(question):
    return f"""You are a Release Readiness Architect.
Focus only on: Final evaluation, Production scoring, Improvement roadmap.
Question: {question}"""

def run_demo():
    print("Initializing Mix Architect AI Agents...\n")
    time.sleep(1.5)
    
    scenarios = [
        {
            "question": "My mix sounds flat.",
            "agent": "Depth Architect",
            "answer": "Your instruments occupy the same perceived distance.\nCreate:\nFront = Lead Vocal\nMiddle = Chords"
        },
        {
            "question": "My mix bus clips.",
            "agent": "Gain Staging Architect",
            "answer": "Target -6 dB headroom before mastering.\nCheck your sub-bass levels and use a clipper on the drum bus."
        },
        {
            "question": "Is this song release ready?",
            "agent": "Release Readiness Architect",
            "answer": "Gain Staging: 8/10\nDepth: 6/10\nFocus: 9/10\nOverall: 7.6/10\nRecommendation: Widen the chorus and reduce vocal reverb."
        }
    ]

    for scenario in scenarios:
        print(f"Question:\n{scenario['question']}\n")
        time.sleep(1)
        print(f"Agent:\n{scenario['agent']}\n")
        time.sleep(1.5)
        print(f"Answer:\n{scenario['answer']}")
        print("\n" + "-"*40 + "\n")
        time.sleep(2.5)
        
    print("Demo complete. Ready for deployment.")

if __name__ == "__main__":
    run_demo()
