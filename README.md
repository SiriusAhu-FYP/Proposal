# FYP Proposal (DDL: 2025-11-21)

This README.md is to help me to clearly organize and manage the contents of my FYP proposal, and also to contribute to the future dissertation writing.

## ⭐ What I'm going to do
Misunderstandings:
- An AI-streamer agent that can play games by itself? ❌ No!
- An AI agent that can play games by telling what to do? ❌ No!

Real Goal:
An AI companion (**partner**) that play game with the user, with 3 core features: 
1. **Proactive Companionship**: "Hey bro, you just missed a chance to be rich!". The partner can proactively spot important events and notify the user.
2. **Collaborative Problem-Solving**: "You've stucked here for a while, do you want me to search some guides for you?" The partner can provide tactical guidance to help the user overcome challenges (with internet search if necessary).
3. **On-Demand Task Delegation**: User: "My mom is calling me for dinner, can you help me to explore the new area?" The partner can temporarily take over some simple tasks to assist the user.

## About the Contents

**Based on the FYP proposal template provided by school**, we should have 4 main sections.

And here I record **my understanding** of each section and subsections. (How will I write them? What to include?)

### Abstract
TODO: TBD

### Glossary Alignment (Optional)
TODO: TBD
1. GCC: General Computer Control, a human-homorphic
2. Skill: The skill / tool set that an agent can use. Also named macro in some literatures.
...

### 1. Introduction
> Demand of interactive & companion experiences (Market possibility) -> Game aspect support: Indie games & Big companies -> Stream / Tech(? not sure) aspect support: Neuro-sama and related open-source community (success on market and tech) -> Vision of Project -> Tech scope -> Summary

1. Point out the demand for **interactive and companion experiences** for entertainment is shifting: **from simple automation / static overlays -> genuine engagement & companionship**.

2. a) Game aspect support: Both single games like `AI2U` (\cite{ai2u_game}) and big companies like `NVIDA` and `Ubisoft` are focusing on building interactive NPCs to enhance user experience (\cite{nvidia_ace_autonomous_2025, ubisoft_neo_npc_2024}).
  - Evidence of AI contributes to actual market value \cite{inworld_market_validation_2023}

3. b) Streaming & tech aspect support: The success of AI-driven virtual streamer `Neuro-sama` demonstrates a growing market (\cite{neurosama_youtube, streamelements_state_2024, streamscharts_q4_2024_landscape}), plus it inspires a vibrant open-source ecosystem (\cite{open_llm_vtuber, airi_project, kimjammer_neuro}).
  - A commercial evidence: \cite{neurosama_hype_streamscharts_2025}
  - i.e. support such demand by market and tech community evidence.

4. Vision of project: 
   - **full voice-loop**
   - a) **proactive, contextual companionship** 
   - b) **collaborative problem-solving** 
   - c) **on-demand task delegation**.
5. Tech scope: 
  - a) **a Unified Action Interface via GUI (GCC)** \cite{CRADLE, ui-venus} 
  - b) **Constrained Action Generation with Structured Output** \cite{Benchmarking-VLA-VLM} 
  - c) **Low-Coupling Orchestration** \cite{ORAK} <- cite this for "abliation framework" idea
6. Summary of this section

### 2. Literature Review
See [Literature_Review.md](Literature_Review.md) for details.

### 3. Methodology

- Outline this project is timely (<span style="background-color:red">Consider whether to remove this paragraph</span>)
  - **Unified evaluation protocols & Modular ablation frameworks** provided by \cite{ORAK, lmgame-bench}
- **GCC availability** proved by \cite{CRADLE, ui-venus}

### 4. Project Plan
##### Objectives
Develop a GCC-based prototype:
  - a) Core functions: Event spotting + Tactical guidance + Voice Loop
  - b) Use MCP-style orchestration to implement "plug-and-play" modules
    - with at least these 4 core modules: skills, planning, memory and reflection

Define some metrics to measure the performance of the prototype
  - e.g., pass@k (pass at k-th attempt), Invalid% (Timesteps with invalid preds / Total number of timesteps) \cite{Benchmarking-VLA-VLM} ⚠️ Many metrics available here

##### Deliverables
1. A system protype, featuring agentic modules, a GUI executor, and safety guards.
2. Evaluation scripts
3. User docs and demos (videos)


#### 1.4 Design Principles & System Preview

<div style="background-color:red">Put to Section 3. Project Plan, or just remove?</div>

**Principles**:
1. `Unified Input`
2. `Structured Output with Constrained Action Selection`
3. `Low-Coupling Orchestration`

**System Preview**:
Explain how the system works. (maybe with a diagram)

### 5. Conclusion

# TODOs
## Revise Suggestions from Supervisor
- [x] Consider remove "timely" part, or put it to Lit. Review section
- [x] Move 1.2 to Lit. Review section
- [ ] Summarize some more detailed classes of these challenges
- [x] Remove "Exclusion" of Scope
- [x] Move 1.3 ("Project Objectives", "Expected Deliverables") and 1.4 to section 3 Project Plan
- [x] Consider remove Glossary section, but keep the contents for the writing of dissertation.
- [x] Add a "Methodology" section before "Project Plan" (not following the template). Introduce how will we implement the system, involve more theory content.
- [ ] Add more citations, to about 30+

## Check the correctness of points in Lit. Review
- [ ] Theme 1
- [ ] Theme 2
- [ ] Theme 3