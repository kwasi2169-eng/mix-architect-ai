# Mix Architect AI — Technical Architecture & Multi-Agent Specification

## 1. System Overview & Target Persona
* **Target User**: Bedroom music producers preparing a stereo mix for release without access to acoustically treated commercial studios or high-end mastering chains.
* **Core Philosophy**: Production decisions supersede plugin tweaks. Mix Architect AI acts as a **decision-support copilot** providing objective structural recommendations. It does *not* claim to create "top-grade" or automated sound; it equips creators with disciplined audio engineering workflows that must be validated with critical listening.

---

## 2. Multi-Agent Team & Information Flow

The architecture consists of three specialized domain architects and an orchestrating conflict-resolution architect.

```mermaid
flowchart TD
    User["Bedroom Producer Input\n(Genre, Track Count, Peak dBFS, Integrated LUFS, Mix Concerns)"] --> Dispatcher["Input Parser & Profile Dispatcher"]
    
    subgraph Specialists ["Domain Specialists"]
        Dispatcher --> GS["1. Gain Staging Architect\n(Headroom, Signal Flow, Clipping Prevention)"]
        Dispatcher --> DA["2. Depth Architect\n(Planes of Depth, Reverb Filtering, Spatial Design)"]
        Dispatcher --> FA["3. Focus Architect\n(Listener Attention, Frequency Hierarchy, Masking)"]
    end
    
    GS --> RR["4. Release Readiness Architect (Orchestrator)\n* Ingests All Domain Directives\n* Detects Inter-Agent Conflicts\n* Applies Subtractive Mediation Engine\n* Runs Fixed Evaluation Checklist"]
    DA --> RR
    FA --> RR
    
    RR --> Plan["Prioritized Action Roadmap\n(Priority 1: Structural Headroom\nPriority 2: Frequency Carving\nPriority 3: Depth Discipline\nPriority 4: A/B Critical Listening Check)"]
```

---

## 3. Specialized Agent Roles & System Prompts

### Agent 1: Gain Staging Architect
* **Domain**: Signal flow, dynamic range integrity, inter-sample clipping prevention, and ear-monitoring safety.
* **System Prompt**:
  ```text
  You are the Gain Staging Architect.
  Primary Objective: Ensure uncompromised headroom (-6 dBFS true peak target for pre-mastering),
  prevent inter-sample clipping, identify sub-bass energy accumulation, and safeguard ear health.
  Never recommend pushing master limiters. Advise on sub-mix gain structure and source level management.
  ```

### Agent 2: Depth Architect
* **Domain**: 3-dimensional front-to-back placement, early reflections vs. late diffuse reverberation, and low-mid clutter mitigation.
* **System Prompt**:
  ```text
  You are the Depth Architect.
  Primary Objective: Construct three clear depth planes (Foreground = dry/intimate, Midground = subtle early reflections,
  Background = diffuse decay). Eliminate muddy reverb buildup in the low-mids (200-500 Hz).
  Preserve transient punch while creating immersive width.
  ```

### Agent 3: Focus Architect
* **Domain**: Listener attention management, frequency masking mitigation, and verse-to-chorus dynamic contrast.
* **System Prompt**:
  ```text
  You are the Focus Architect.
  Primary Objective: Direct listener attention to the singular emotional focal point (lead vocal or lead motif).
  Resolve frequency masking and create dynamic contrast between song sections.
  ```

### Agent 4: Release Readiness Architect (Orchestrator & Conflict Resolver)
* **Domain**: Multi-agent arbitration, conflict mediation, and roadmap prioritization.
* **System Prompt**:
  ```text
  You are the Release Readiness Architect.
  Primary Objective: Act as the lead production supervisor. Mediate conflicting recommendations from
  Gain Staging, Depth, and Focus architects. Synthesize an actionable, prioritized execution plan.
  Always position recommendations as decision support requiring producer validation and critical listening.
  ```

---

## 4. Conflict Resolution Engine

In traditional mixing, domain goals often directly clash. The Release Readiness Architect detects and arbitrates these conflicts:

| Conflicting Agents | The Conflict | Naive / Harmful Solution | Mix Architect AI Resolution (Mediation) | Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Gain Staging vs. Focus** | Focus wants vocal louder and more prominent, but Gain Staging flags headroom is already exhausted (peak > -3 dBFS). | Raising vocal fader or adding master limiter gain, causing inter-sample distortion. | **Subtractive Carving**: Pull back masking rhythm guitars/synths by -2.5 dB and carve a 2.5 kHz dynamic pocket. | Yields +2.5 dB perceived vocal prominence without consuming any additional mix bus headroom. |
| **Depth vs. Focus** | Depth wants rich, lush plate reverb for ambient space, but Focus warns the wash buries chorus punch and diction. | Muting the reverb (flat mix) or keeping it wet (muddy mix). | **Ducked Pre-Delay Routing**: High-pass reverb return at 600 Hz, set 60ms pre-delay, and sidechain-compress return bus (-3 dB during vocal phrases). | Dry transient cuts through immediately; lush ambience blossoms only in the gaps between words. |

---

## 5. Security & Privacy Assurance
* **No Credential Leaks**: Zero API keys or hardcoded credentials exist in this codebase.
* **Git Hygiene**: Strict `.gitignore` prevents inadvertent commits of `.env` files, audio project sessions (`.wav`, `.aiff`, `.flac`), and local configurations.
* **Local Execution**: All processing is local and deterministic; no producer audio stems or intellectual property are transmitted to external servers.
