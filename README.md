# Mix Architect AI

> **A Multi-Agent Decision Support System for Bedroom Music Producers Preparing Stereo Mixes for Release**

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Standard%20Library-brightgreen.svg)]()

---

## 1. Problem & Target Audience

### The Target User
A **bedroom music producer** mixing and preparing a stereo track for commercial release (Spotify, Apple Music, SoundCloud) without access to multi-million-dollar acoustic rooms or hardware mastering chains.

### The Real-World Challenge
Producers frequently spend endless hours tweaking microscopic compressor settings or swapping equalizers while overlooking macro **production architecture**:
* Depleted mix bus headroom leading to inter-sample clipping on streaming encoders.
* Flat, two-dimensional soundscapes where all instruments fight for the same front-row acoustic space.
* Lead vocals getting buried under competing mid-range instruments in dense choruses.
* Uncontrolled sub-bass frequencies eating dynamic range and causing playback distortion on small speakers.

### Our Solution
**Mix Architect AI** departs from generic "magic fix" plugins by introducing a **collaborative team of specialized AI agents**. The system ingests structured mix metadata and outputs a prioritized, conflict-resolved architectural action plan.

> **Positioning Notice**: Mix Architect AI is a **decision-support tool**. It does not promise "top-grade" automated sound with a single click. Audio engineering requires critical listening, speaker calibration, and producer judgment; this system provides the disciplined decision framework to guide those ears.

---

## 2. System Inputs, Process & Outputs

```
+--------------------------------------------------------------------------+
|                               USER INPUTS                                |
|  * Genre: e.g., Indie Pop, Trap, Folk                                    |
|  * Track Count: Number of active stems / audio tracks                    |
|  * Peak Reading (dBFS): True peak level on mix bus                       |
|  * Integrated Loudness (LUFS): Integrated loudness level                 |
|  * Mix Concerns: Specific pain points (e.g., "buried vocal", "flat mix") |
+--------------------------------------------------------------------------+
                                     |
                                     v
+--------------------------------------------------------------------------+
|                             MULTI-AGENT PROCESS                          |
|  1. Gain Staging Architect   -> Checks headroom & inter-sample risks     |
|  2. Depth Architect          -> Establishes 3-tier spatial planes        |
|  3. Focus Architect          -> Identifies frequency masking & focal tier|
|  4. Release Readiness Engine -> Detects & mediates agent conflicts       |
+--------------------------------------------------------------------------+
                                     |
                                     v
+--------------------------------------------------------------------------+
|                                OUTPUTS                                   |
|  * Diagnosis per architectural domain                                    |
|  * Transparent conflict resolution report (with engineering rationale)   |
|  * Prioritized Action Roadmap (Priority 1: Structural -> Priority 4)     |
|  * 4-Point Evaluation Checklist verification                             |
+--------------------------------------------------------------------------+
```

---

## 3. The Specialist Agent Team

| Agent | Focus Area | Core Objective | Key Principle |
| :--- | :--- | :--- | :--- |
| **Gain Staging Architect** | Headroom & Signal Flow | Target -6.0 dBFS True Peak pre-master ceiling | Fix levels at stem sources; never rely on master fader drops. |
| **Depth Architect** | Spatial Dimension & Reverbs | Construct 3 depth planes (Foreground, Midground, Background) | Filter reverb returns (HPF 600 Hz / LPF 6 kHz) to prevent low-mid wash. |
| **Focus Architect** | Attention & Masking | Establish strict hierarchy (Lead Vocal = Tier 1) | Practice subtractive dynamic EQ carving on masking instruments. |
| **Release Readiness Architect** | Orchestrator & Conflict Resolver | Synthesize conflicting advice into a single cohesive action plan | Mediate trade-offs (e.g., loudness vs. headroom) with engineering rationale. |

---

## 4. Multi-Agent Conflict Resolution Example

In audio mixing, domain objectives naturally collide. Mix Architect AI includes an explicit mediation layer:

* **The Conflict**: The **Focus Architect** notes the vocal is getting buried in the chorus and needs greater prominence. Meanwhile, the **Gain Staging Architect** detects that the mix bus is already peaking at `-1.2 dBFS` (only 1.2 dB of headroom left).
* **Naive / Damaging Action**: Boosting the vocal fader or pushing a master limiter, which causes inter-sample digital clipping.
* **Mix Architect AI Resolution**: The **Release Readiness Architect** mandates **Subtractive Frequency Carving**:
  > *"Do not raise the vocal fader. Instead, attenuate competing mid-range synths and guitars by -2.5 dB, and apply a 2-3 dB dynamic EQ dip between 1.5 kHz - 3.5 kHz on guitar stems triggered by the vocal."*
* **Result**: Achieves +2.5 dB of perceived vocal intelligibility with **zero** additional headroom consumed.

---

## 5. Quickstart & How to Run

Mix Architect AI was engineered with **zero external dependencies** — it runs out of the box on standard Python.

### Requirements
* **Python**: 3.8 or higher (No `pip install` required).

### Run Test Suite & Demo
Run the automated runner which executes the 3 realistic test cases against the fixed evaluation checklist:
```bash
python mix_architect.py
```

---

## 6. The 3 Realistic Test Cases & Evaluation Benchmark

All recommendations are verified against our fixed **4-Point Evaluation Checklist**:
1. **Technical Accuracy**: Strict alignment with established audio engineering standards (headroom thresholds, masking curves).
2. **Actionability**: Specific numerical adjustments (dB values, filter frequencies, routing topologies) instead of abstract subjective advice.
3. **Consistency**: Harmonized recommendations across stems that avoid conflicting moves.
4. **User Safety**: Protection against ear fatigue, sudden volume overshoots, and tweeter damage.

| Test Case | Genre & Profile | Key Problem | Agent Resolution | Checklist Result |
| :--- | :--- | :--- | :--- | :--- |
| **Case 1: "Sundown Memories"** | Indie Pop (38 tracks, -1.2 dBFS peak) | Vocals buried in chorus; synth wash; flat 2D image | Uniform -4.8 dB stem reduction; Abbey Road reverb filters; 2.5 kHz subtractive vocal pocket | **All 4 Criteria PASSED** |
| **Case 2: "Night Run 808"** | Modern Trap (24 tracks, +1.8 dBFS peak) | Severe true peak clipping; 808 distortion on small speakers | Global -7.8 dB stem attenuation; 28 Hz 24dB/oct sub HPF; dynamic 55 Hz notch on 808 | **All 4 Criteria PASSED** |
| **Case 3: "Cedar & Pine"** | Folk / Acoustic (14 tracks, -5.8 dBFS peak) | Harsh guitar pick transients; dynamic vocal swings | Two-stage vocal compression (opto leveling + VCA peaks); 45ms pre-delay room ambience | **All 4 Criteria PASSED** |

*(For full technical breakdowns and frequency charts, see [TEST_EVALUATIONS.md](TEST_EVALUATIONS.md)).*

---

## 7. Architecture & System Prompts

For full prompt definitions, signal flow diagrams, and routing schemas, refer to:
* **[ARCHITECTURE.md](ARCHITECTURE.md)**: Deep dive into the multi-agent orchestration pattern and full prompt library.

---

## 8. Reflection: Key Iterations & "What Failed"

Building an agentic system for creative disciplines taught us critical lessons:

1. **Failure of Unconstrained LLM Recommendations (Iteration 1)**:  
   *Early prompt drafts suggested plugins by name (e.g. 'add FabFilter Pro-Q 3 or Soundtoys Decapitator'). This failed because bedroom producers often cannot afford high-end commercial plugin suites. We refactored all agent prompts to focus strictly on **fundamental architectural actions** (EQ frequencies, fader levels, pre-delays, sidechain topologies) that can be executed in **any DAW with stock native plugins**.*
2. **The "Everything Upfront" Conflict (Iteration 2)**:  
   *When evaluated independently, the Focus and Depth agents fought each other: Focus made everything louder and upfront, while Depth soaked elements in reverb until all definition disappeared. This demonstrated the vital necessity of an **Orchestrator & Conflict Resolver (Release Readiness Architect)** to balance spatial wetness against transient intimacy.*
3. **The Trap of Promising "Master-Ready Sound"**:  
   *Initial documentation used marketing language like "professional grade sound instantly". We deliberately stripped this out. AI cannot listen to room modes or physical speaker resonance. Positioned honestly as **decision support**, the tool respects the producer's ears and critical listening workflow.*

---

## 9. Security, Privacy & Data Protection

* **Zero API Key Leakage**: No API keys or tokens are stored in the codebase or git tree.
* **Git Hygiene**: Strict `.gitignore` ensures that user audio files (`.wav`, `.aiff`, `.mp3`), DAW project files (`.flp`, `.als`, `.logicx`), and local environment variables (`.env`) are never committed to GitHub.
* **Privacy by Design**: All analysis operates locally on numerical metadata and descriptors without transmitting user audio stems off-device.

---

## 10. License
Distributed under the MIT License. See `LICENSE` for details.
