# Mix Architect AI — Test Cases & Fixed Evaluation Benchmarks

All test cases are benchmarked against four non-negotiable criteria:
1. **Technical Accuracy**: Adherence to standard audio engineering laws (inter-sample peak headroom, Fletcher-Munson curve perception, masking frequencies).
2. **Actionability**: Specific, numbered instructions containing exact decibel adjustments, cutoff frequencies, and signal routings (avoiding vague buzzwords like "make it warmer").
3. **Consistency**: Coherent recommendations across all tracks without conflicting fader moves.
4. **User Safety**: Protection against ear fatigue, monitor blowouts, and digital clipping.

---

## Test Case 1: Bedroom Indie Pop — "Sundown Memories"

### Inputs
* **Target User**: Bedroom indie producer working on laptop & headphones.
* **Genre**: Indie Pop / Dream Pop
* **Track Count**: 38 tracks (dense synth layers, rhythm guitars, stacked vocal harmonies)
* **Peak Reading**: -1.2 dBFS (depleted headroom)
* **Integrated Loudness**: -14.2 LUFS
* **Mix Concerns**: "Vocals sound distant and get lost in the chorus; synths wash out the mix; overall stereo image feels flat and two-dimensional."

### Specialist Outputs
* **Gain Staging Architect**: Flags peak of -1.2 dBFS. Recommends pulling all sub-group faders down by 4.8 dB to restore -6.0 dBFS pre-mastering headroom.
* **Depth Architect**: Identifies cluttered low-mids (200-500 Hz). Mandates Abbey Road Reverb filtering (HPF 600 Hz, LPF 6 kHz) and pushing background synths back via high-shelf roll-off (-2 dB above 8 kHz).
* **Focus Architect**: Identifies vocal masking caused by electric guitar and synth leads in the 1.5–3.5 kHz range during the chorus.

### Conflict Resolution
* **Conflict**: Focus demands vocal prominence, but Gain Staging refuses to allow vocal fader increases due to lack of headroom.
* **Resolution**: Subtractive dynamic EQ carving (-2.5 dB cut on synth stems sidechained to lead vocal). Vocal becomes effortlessly audible with zero headroom penalty.

### Evaluation Checklist
| Criterion | Status | Verification Note |
| :--- | :--- | :--- |
| **Technical Accuracy** | **PASSED** | Adheres to pre-master headroom standard (-6 dBFS) and masking frequency mitigation. |
| **Actionability** | **PASSED** | Exact frequencies (600 Hz / 6 kHz filters, 2.5 kHz dip) and relative dB targets provided. |
| **Consistency** | **PASSED** | Depth and Focus directives complement each other without competing spatial claims. |
| **User Safety** | **PASSED** | Ear-safety reminder on headphone monitoring levels and headphone fatigue prevention. |

---

## Test Case 2: Modern Trap — "Night Run 808"

### Inputs
* **Target User**: Home producer preparing an aggressive beat for streaming delivery.
* **Genre**: Modern Trap / Hip-Hop
* **Track Count**: 24 tracks
* **Peak Reading**: +1.8 dBFS (Severe True Peak digital clipping)
* **Integrated Loudness**: -9.5 LUFS
* **Mix Concerns**: "Mix bus is constantly clipping red; 808 bass distorts uncontrollably on phone and laptop speakers; master limiter chokes and pumps."

### Specialist Outputs
* **Gain Staging Architect**: Critical alarm on +1.8 dBFS overload. Recommends global stem reduction of 7.8 dB to achieve -6 dBFS headroom. Directs steep 24 dB/oct HPF at 28 Hz to cut sub-audible infrasound.
* **Depth Architect**: Keeps 808, kick, and snare 100% dry and centered in the foreground plane to preserve maximum transient punch.
* **Focus Architect**: Manages kick vs. 808 collision. Directs dynamic notch on 808 at 55 Hz triggered by kick drum transient.

### Conflict Resolution
* **Conflict**: Pushing loudness (-9.5 LUFS) vs. Gain Staging clipping prevention (+1.8 dBFS).
* **Resolution**: Strip master bus limiter entirely during mixdown. Achieve perceived density using parallel saturation and soft-clipping on drum bus instead of hard digital peak limiting.

### Evaluation Checklist
| Criterion | Status | Verification Note |
| :--- | :--- | :--- |
| **Technical Accuracy** | **PASSED** | Eliminates inter-sample clipping and addresses low-frequency speaker translation laws. |
| **Actionability** | **PASSED** | Specific HPF slope (24 dB/oct @ 28 Hz) and sidechain frequency (55 Hz). |
| **Consistency** | **PASSED** | Drum bus and 808 processing aligned without phase cancellation. |
| **User Safety** | **PASSED** | Prevents harsh transient spikes that damage studio monitor tweeters or listener ears. |

---

## Test Case 3: Acoustic Singer-Songwriter — "Cedar & Pine"

### Inputs
* **Target User**: Solo artist mixing acoustic guitar and vocals in an untreated room.
* **Genre**: Folk / Acoustic
* **Track Count**: 14 tracks
* **Peak Reading**: -5.8 dBFS
* **Integrated Loudness**: -21.5 LUFS
* **Mix Concerns**: "Acoustic guitar pick clicks are harsh and piercing; vocal volume fluctuates drastically between whisper verses and belted chorus; mix lacks warmth."

### Specialist Outputs
* **Gain Staging Architect**: Headroom is healthy (-5.8 dBFS). Directs producer to maintain current gain structure and avoid artificial gain boosts.
* **Depth Architect**: Recommends short chamber/room reverb with 45ms pre-delay to add natural body and simulated room acoustic warmth without pushing vocals into the distance.
* **Focus Architect**: Directs serial two-stage vocal compression (optical compressor for smooth leveling followed by fast VCA compressor catching 2 dB peaks) to tame dynamic spread between verse and chorus.

### Conflict Resolution
* **Directives Aligned**: No architectural contradiction detected between agents.

### Evaluation Checklist
| Criterion | Status | Verification Note |
| :--- | :--- | :--- |
| **Technical Accuracy** | **PASSED** | Two-stage compression preserves natural vocal timbre without squashing dynamics. |
| **Actionability** | **PASSED** | Exact pre-delay timing (45ms) and two-stage compressor topology clearly instructed. |
| **Consistency** | **PASSED** | Guitar and vocal dynamic profiles balanced across both sections. |
| **User Safety** | **PASSED** | Tames harsh 3–4 kHz acoustic pick transients that trigger listener fatigue. |
