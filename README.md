# AI-Based Online Assessment Proctoring System with Intelligent Cheating Risk Assessment

**Group ID:** BSEF23-07
**Program:** Bachelor of Science in Software Engineering (2023–2027)
**Department of Software Engineering, Faculty of Computing & Information Technology (FCIT), University of the Punjab, Lahore**
**Supervisor:** Dr Natalia Chaudhary, Assistant Professor

A full-stack platform that lets companies run secure online assessments (coding tests, MCQs, aptitude tests) from anywhere, while an AI proctoring pipeline verifies candidate identity, checks the exam environment, monitors behaviour throughout the exam, and produces a single explainable **Low / Medium / High** risk report — cutting the need for live human invigilators and the false-positive alerts common in existing tools.

---

## Table of Contents

1. [Abstract](#1-abstract)
2. [Problem Statement & Motivation](#2-problem-statement--motivation)
3. [Project Objectives](#3-project-objectives)
4. [System Overview](#4-system-overview)
   - [4.1 Company (Recruiter) Portal](#41-company-recruiter-portal)
   - [4.2 Candidate Portal](#42-candidate-portal)
   - [4.3 Identity Verification Module](#43-identity-verification-module)
   - [4.4 Room Verification Module](#44-room-verification-module)
   - [4.5 Phone Placement Verification Module](#45-phone-placement-verification-module)
   - [4.6 Live AI Monitoring Module](#46-live-ai-monitoring-module)
   - [4.7 Smart Audio Monitoring Module](#47-smart-audio-monitoring-module)
   - [4.8 Behaviour Risk Analysis System](#48-behaviour-risk-analysis-system-core-contribution)
   - [4.9 AI Report Module](#49-ai-report-module)
   - [4.10 End-to-End Workflow](#410-end-to-end-workflow)
5. [AI / ML Architecture](#5-ai--ml-architecture)
6. [Tech Stack](#6-tech-stack)
7. [Project Structure](#7-project-structure)
8. [Getting Started](#8-getting-started)
9. [Team & Roles](#9-team--roles)
10. [Development Methodology](#10-development-methodology)
11. [Sprint Plan (24 Weeks)](#11-sprint-plan-24-weeks)
12. [Timeline / Milestones](#12-timeline--milestones)
13. [Market Fit / Commercial Potential](#13-market-fit--commercial-potential)
14. [Competitor Positioning](#14-competitor-positioning)
15. [Branching Strategy & Git Workflow](#15-branching-strategy--git-workflow)
16. [Repository Setup Checklist](#16-repository-setup-checklist)
17. [Supervisor & Approval](#17-supervisor--approval)

---

## 1. Abstract

Many IT companies now screen candidates with online tests before interviews, but have no reliable way to confirm the person taking the test is who they claim to be, or that they're taking it honestly. Off-the-shelf proctoring platforms are built for large international markets, priced accordingly, and tend to flag ordinary behaviour (glancing away for a second, background noise) as suspicious.

This project delivers a **low-cost AI-based online assessment platform built for Pakistani companies**. Companies create and schedule assessments and invite candidates by email; candidates verify their identity and environment, sit the exam under continuous AI observation, and the system automatically produces a behaviour report. The core contribution is a **custom rule-based Behaviour Risk Analysis System** that fuses signals from every AI module into one overall risk score, rather than showing recruiters a wall of disconnected warnings.

## 2. Problem Statement & Motivation

- Companies increasingly hire remotely and need a trustworthy way to run online tests.
- It's difficult to know whether a candidate is being honest or receiving outside help during an unsupervised online exam.
- Existing proctoring systems are expensive and largely designed for international markets, not Pakistani companies.
- Many existing systems over-flag normal activity (e.g. looking left briefly, ambient sound), creating noisy, low-trust reports.

**Goal:** build a low-cost AI-based online assessment system that monitors candidates, minimizes false alerts, and gives companies a clear, evidence-backed report to support their hiring decision.

## 3. Project Objectives

- Build a complete online assessment platform for companies and candidates.
- Allow companies to create, schedule, and manage online assessments.
- Send automated invitation emails to candidates with assessment details.
- Provide a candidate portal for registration, login, and viewing upcoming assessments.
- Verify candidate identity before the exam via face verification.
- Perform room and desk verification before the exam starts.
- Verify the candidate's mobile phone is placed away from the exam area.
- Continuously monitor the candidate during the exam using AI.
- Detect head movement, eye movement, multiple people, phones, and other unauthorized objects.
- Detect browser tab switching and other browser-level violations during the exam.
- Analyze audio and flag only suspicious sound events (ignoring normal background noise).
- Develop a rule-based Behaviour Risk Analysis System that combines scores from pretrained AI models to reduce false alerts.
- Generate an AI report with flagged events and an overall risk score for the company.

**Success criteria:** all modules completed and integrated, candidates correctly monitored during live assessments, accurate AI reports generated after each assessment, and a measurable reduction in false alerts via the Behaviour Risk Analysis System.

## 4. System Overview

The system has two primary user types — **Company** and **Candidate** — supported by a set of AI modules that verify, monitor, and report on the candidate throughout the assessment lifecycle.

### 4.1 Company (Recruiter) Portal

Companies manage the entire assessment lifecycle:

- Register and log in
- Create online assessments and upload questions
- Schedule exam date, time, and duration
- Add/invite candidates by email
- Configure allowed materials (e.g. calculator, rough sheets) vs. prohibited items
- View candidate results, AI monitoring reports, and flagged events
- Make the final hiring decision

*Example configuration:* "Frontend Developer Assessment" · 90 minutes · Allowed: scientific calculator, two blank pages · Not allowed: mobile phone, books, smart watch.

### 4.2 Candidate Portal

Candidates interact with a focused, guided flow:

- Register and log in
- View all scheduled assessments with a live countdown ("Starts in 2 Days, 5 Hours, 18 Minutes")
- Read exam instructions
- Complete identity, room, and phone-placement verification
- Start the assessment once the scheduled time unlocks the **Start Assessment** button
- Submit the assessment — once submitted, the exam is permanently locked and cannot be reopened

### 4.3 Identity Verification Module

**Purpose:** confirm the registered candidate is the one taking the exam.

**Flow:** candidate shows a CNIC/passport to the webcam → the AI compares the ID photo against the live webcam face → if both faces match, verification succeeds and the candidate proceeds; otherwise the exam cannot begin.

### 4.4 Room Verification Module

**Purpose:** confirm the exam environment satisfies company rules before the exam starts.

The candidate is asked to slowly show, via webcam:

- The complete room and surrounding area
- Walls and entrance door
- The desk and chair, including under the table if needed
- Allowed items only (e.g. calculator, blank rough sheets), if permitted

This step ensures no unauthorized people or objects are present before the exam begins.

### 4.5 Phone Placement Verification Module

One of the system's distinguishing features. The candidate is guided to:

1. Show the mobile phone to the camera
2. Place it visibly out of arm's reach of the exam desk
3. Return to the chair and show both hands
4. Show the desk and chair again for confirmation

The candidate may not leave their seat again after this step. This directly targets one of the most common cheating vectors in unsupervised exams.

### 4.6 Live AI Monitoring Module

Once verification completes, the exam begins and the AI observes continuously without interrupting the candidate. It never declares cheating on its own — it records events for the risk engine to interpret. Monitored signals include:

| Signal | What's tracked |
|---|---|
| Face visibility | Whether the candidate's face stays inside the camera frame |
| Continuous identity check | Re-verifies live face against the registered candidate at intervals; a mismatch is a serious violation |
| Head pose | Yaw / pitch / roll — repeated looking left, right, or up is logged (looking down is allowed, for writing on paper) |
| Eye gaze | Looking at the screen is normal; repeated looking left/up is flagged, looking down is allowed |
| Object detection | Phones, books, tablets, extra laptops, smart watches, and other unauthorized items |
| Multiple-person detection | Expects exactly one person in frame at all times |
| Seat / presence monitoring | Flags extended candidate absence from the seat |
| Browser monitoring | Tab switching, window minimize, dev tools, copy/paste, fullscreen exit |

### 4.7 Smart Audio Monitoring Module

Rather than flagging every sound, the system classifies audio events:

- Human voices → flagged
- Door-opening sounds → flagged
- Ambient noise (fans, traffic, distant sounds) → ignored

This keeps the candidate's report focused on genuinely suspicious audio rather than normal household noise.

### 4.8 Behaviour Risk Analysis System (core contribution)

Instead of raising a separate warning for every flagged event, this module combines **all** signals from the exam — head movement, eye movement, phone detection, face visibility, voice detection, door events, browser activity, seat absence, and multiple-person detection — through a **rule-based scoring engine** with predefined thresholds, and produces one overall behaviour risk level:

- **Low Risk**
- **Medium Risk**
- **High Risk**

This is a shared module built collaboratively by all three team members, covering:

- Collecting output values/confidence scores from every AI module
- Deciding risk rules and threshold values per event type (e.g. how many tab switches count as risky, how many seconds of missing face counts as risky)
- Designing the rule engine that combines multiple flagged events into a single score
- Manually walking through candidate scenarios (normal candidate, candidate using a phone, candidate leaving the seat, etc.) to sanity-check and tune the rules
- Wiring the rule engine into the backend so it runs automatically during and after the exam
- Producing the final Behaviour Risk Score for the company

### 4.9 AI Report Module

After submission, the system automatically compiles a complete behavioural report containing:

- Candidate information and assessment result
- Identity verification status
- Flagged events with timestamp, confidence score, screenshot, and short video clip
- Violation timeline and evidence
- Overall risk level (Low / Medium / High)

*Example event:* `10:15:22 — Phone Detected — Confidence 97% — Screenshot saved — 15s video clip`.

The **Recruiter Dashboard** surfaces this report so the company reviews only the important moments instead of watching a full 90-minute recording, and makes the final hiring call.

### 4.10 End-to-End Workflow

```
Company creates & schedules assessment
        ↓
Invitation email sent to candidate (login link, credentials, schedule, instructions)
        ↓
Candidate logs in → sees countdown to exam
        ↓
At scheduled time → Identity Verification → Room Verification → Phone Placement Verification
        ↓
Exam starts → Live AI Monitoring (face, head pose, eye gaze, objects, people, browser, audio)
        ↓
Events streamed continuously → Behaviour Risk Analysis System
        ↓
Candidate submits → exam locked permanently
        ↓
AI Report Module generates report (events, evidence, risk level)
        ↓
Recruiter Dashboard → company reviews evidence → final hiring decision
```

## 5. AI / ML Architecture

Every model is a specialized, pretrained perception module — the application layer interprets raw model outputs against examination rules rather than treating any single output as a cheating verdict.

| Task | Input | Output | Model | Training Required |
|---|---|---|---|---|
| Face verification | ID photo + live webcam frame | Verified (true/false), confidence | DeepFace (ArcFace) | No — pretrained |
| Face detection & landmarks | Webcam frame | Face coordinates, landmarks | MediaPipe Face Detection / Face Mesh | No — pretrained |
| Head pose estimation | Face landmarks | Yaw, pitch, roll, direction | MediaPipe Face Mesh | No — pretrained |
| Eye gaze estimation | Eye landmarks | Looking left/right/up/down | MediaPipe Iris | No — pretrained |
| Object detection | Webcam frame | Object class, confidence, bounding box | YOLOv11 | No — pretrained |
| Person counting | Webcam frame | Number of persons in frame | YOLOv11 | No — pretrained |
| Voice activity detection | Microphone audio | Speech / no speech / multiple voices | Silero VAD | No — pretrained |

**Example inference chain:**

```
Webcam Frame → YOLOv11 → "Phone, 97% confidence, bounding box" → Rule Engine → Flag Event
Webcam Frame → MediaPipe → facial landmarks → head-direction calculation → Rule Engine → Flag/Allow
ID Photo + Webcam Frame → DeepFace → "Verified = True, Confidence = 0.94" → App decides candidate can proceed
```

Models act purely as perception modules; the **Behaviour Risk Analysis System** is where examination policy is actually applied.

## 6. Tech Stack

| Layer | Technologies / Tools |
|---|---|
| Frontend | Next.js (React), TypeScript, Tailwind CSS, HTML, CSS, JavaScript |
| Backend | NestJS, Node.js, TypeScript, REST APIs, JWT Authentication, bcrypt |
| Database | PostgreSQL, Prisma ORM |
| AI / Machine Learning | MediaPipe (Face Detection, Face Mesh, Iris), DeepFace (ArcFace), OpenCV, YOLOv11 (object detection) |
| Email Services | Nodemailer, Gmail SMTP |
| Dev Tools | Git, GitHub, Postman, VS Code, Docker (optional), Prisma Studio |
| Testing Tools | Jest (NestJS), Postman |
| Deployment | Vercel (frontend), Render or Railway (backend), PostgreSQL cloud database |

## 7. Project Structure

Proposed layout — refine once architecture decisions (e.g. whether the AI/ML code runs as a separate Python service vs. embedded scripts) are locked in during Sprint 1–2:

```
.
├── frontend/                # Next.js — Company Portal, Candidate Portal, exam UI
│   ├── app/
│   ├── components/
│   └── ...
├── backend/                  # NestJS — REST APIs, auth, business logic
│   ├── src/
│   │   ├── auth/
│   │   ├── companies/
│   │   ├── candidates/
│   │   ├── assessments/
│   │   ├── monitoring/       # endpoints receiving AI module events
│   │   └── risk-engine/      # Behaviour Risk Analysis System
│   └── prisma/                # schema.prisma & migrations
├── ai-service/                # Python — DeepFace, MediaPipe, YOLOv11, Silero VAD inference
├── docs/                       # Proposal, diagrams, sprint reports, meeting notes
│   └── FYDP_PROJECT_PROPOSAL.pdf
├── .github/                    # Issue templates, PR templates, workflows (optional CI)
└── README.md
```

## 8. Getting Started

> This section describes the anticipated local setup and will be filled in with real commands/scripts as each module lands, starting Sprint 1–2.

**Prerequisites:** Node.js 18+, PostgreSQL, npm or yarn, Python 3.10+ (for the AI service), Git.

```bash
# 1. Clone the repository
git clone https://github.com/<org-or-user>/<repo-name>.git
cd <repo-name>

# 2. Backend — NestJS + Prisma
cd backend
npm install
cp .env.example .env
# Set in .env: DATABASE_URL, JWT_SECRET, SMTP_USER, SMTP_PASS, etc.
npx prisma migrate dev
npm run start:dev

# 3. Frontend — Next.js (new terminal)
cd frontend
npm install
cp .env.example .env.local
# Set: NEXT_PUBLIC_API_URL=http://localhost:<backend-port>
npm run dev

# 4. AI service — Python (new terminal, once implemented)
cd ai-service
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python main.py
```

**Running tests:**

```bash
cd backend
npm run test        # Jest unit tests
```

## 9. Team & Roles

| Name | Roll Number | Email | Scrum Role | Core Ownership |
|---|---|---|---|---|
| Hamda Ahmad | BSEF23A042 | bsef23a042@pucit.edu.pk | Product Owner & Developer | Company/Candidate Portal, Login & Registration (frontend); Face Verification, ID Verification, Room Verification, Desk Verification, Phone Placement Verification (AI); Auth APIs, User Management, Company & Candidate APIs, database design (backend) |
| Abdullah Naeem | BSEF23A036 | bsef23a036@pucit.edu.pk | Developer | Dashboard, Assessment Creation, Assessment Scheduling (frontend); Door Monitoring, Head Pose Detection, Eye Movement Detection, Multiple Person Detection (AI); Assessment APIs, Question Management, Scheduling APIs, AI Monitoring APIs (backend) |
| Noor Fatima | BSEF23A041 | bsef23a041@pucit.edu.pk | Scrum Master & Developer | Countdown Timer, Email Invitations, UI/UX (frontend); Unauthorized Object Detection, Browser Tab Detection, Audio Monitoring (AI); Results APIs, Report Generation, Recordings, Risk Score APIs (backend) |

**Shared module (all members):** Behaviour Risk Analysis System — see [Section 4.8](#48-behaviour-risk-analysis-system-core-contribution).

## 10. Development Methodology

**Agile Scrum**, chosen because the project spans many interdependent modules and AI features that benefit from incremental delivery and continuous feedback.

- **Duration:** 24 weeks, split into 12 sprints of 2 weeks each
- **Sprint activities:** Sprint Planning → Daily Stand-up → Sprint Review/Demo → Sprint Retrospective
- **Product backlog:** prepared up front, prioritized by importance, and updated after every sprint based on completed work and supervisor feedback

| Role | Member | Responsibilities |
|---|---|---|
| Product Owner | Hamda Ahmad | Manages requirements, prepares the product backlog, prioritizes features, ensures the system meets project goals |
| Scrum Master | Noor Fatima | Organizes sprint meetings, tracks progress, removes blockers, coordinates with the supervisor |
| Developers | Hamda Ahmad, Abdullah Naeem, Noor Fatima | Design, develop, test, and integrate all frontend, backend, AI, and ML modules |

## 11. Sprint Plan (24 Weeks)

| Sprint | Weeks | Main Work |
|---|---|---|
| 1 | 1–2 | Gather requirements, finalize scope, system & database design |
| 2 | 3–4 | Login, registration, authentication, company/candidate portals |
| 3 | 5–6 | Assessment creation, scheduling, email invitations, dashboard |
| 4 | 7–8 | Face verification, ID verification, room verification, desk verification |
| 5 | 9–10 | Head pose detection, eye movement detection, multiple person detection, object detection |
| 6 | 11–12 | Phone placement verification, browser monitoring, door monitoring, audio monitoring |
| 7 | 13–14 | Define risk rules, thresholds, and scoring logic from each AI module's outputs |
| 8 | 15–16 | Implement, test, and validate the rule-based risk scoring engine against sample scenarios |
| 9 | 17–18 | Integrate all AI modules with the backend; generate AI reports and risk scores |
| 10 | 19–20 | Complete testing, fix bugs, improve performance, optimize the system |
| 11 | 21–22 | Final documentation, deployment, presentation preparation, final submission |

## 12. Timeline / Milestones

| Milestone | Tasks | Expected Outcome |
|---|---|---|
| Proposal Submission (D0) | Finalize idea, literature review, problem statement, requirements, proposal document & presentation | Approved FYP proposal |
| D1 — System Design & Prototyping | System architecture, DB schema, UI wireframes, use case diagrams; design Company/Candidate Portal, AI workflow, Risk Analysis workflow; basic working prototype | Complete system design + working prototype |
| D2 — Working Core / MVP | Frontend & backend build-out: auth, portals, assessment creation/scheduling, countdown timer, email invitations, exam interface; integrate identity/room/desk verification and basic AI monitoring | Minimum Viable Product with core features |
| Mid-Semester Evaluation | Demo completed modules, present progress, get supervisor feedback, identify remaining-phase improvements | Evaluation completed |
| D3 — Final Sprint / Deployment Beta | Complete all AI modules (face, phone placement, door, head pose, eye movement, object detection, browser, audio, risk engine); full integration and testing | Beta version of the complete system |
| D4 — Final Product Submission | Final testing, performance optimization, AI report generation, documentation, user manual, installation guide | Final product + full documentation submitted |
| Pre-Evaluation Preparation | Review all modules, code, reports, slides, docs; resolve remaining issues | Ready for final evaluation |
| Final Evaluation | Demo complete system; explain modules, AI models, risk engine, methodology; answer panel questions | Successful project completion |

## 13. Market Fit / Commercial Potential

Software houses, IT companies, universities, and training centers regularly run online tests before hiring or admissions. Most existing proctoring tools target international markets at price points that may not suit smaller Pakistani companies (no formal pricing comparison has been done). This system aims to give such organizations an AI-assisted way to monitor candidates and receive a clear Low/Medium/High risk report. Beyond the FYP, it could potentially evolve into a subscription-based SaaS offering — though that would require further cost analysis, business planning, and validation with real customers before being commercially viable.

## 14. Competitor Positioning

Established platforms like ProctorU, Proctorio, Examity, and Honorlock serve universities and companies internationally. No formal, verified feature-by-feature comparison against these tools has been conducted, so this project avoids specific claims about what they do or don't include. Instead, here's what this system aims to offer:

- Identity verification via face matching before the exam
- Room and desk verification before the exam starts
- Phone placement verification (candidate shows phone placed out of reach)
- Continuous monitoring of head movement, eye movement, and presence during the exam
- Browser-level security (tab switching, fullscreen exit, copy-paste, dev tools detection)
- Audio monitoring for suspicious sounds
- A rule-based system combining all detected events into one overall risk score, rather than many isolated warnings

**Intended positioning:** rather than competing directly with large international platforms, this project targets Pakistani IT companies running online hiring assessments, where a simpler, self-contained monitoring and reporting system may be a good fit. This is the project's intended niche, not a claim of having benchmarked against existing commercial products.

## 15. Branching Strategy & Git Workflow

`main` stays deployable at all times. Work happens on sprint/module-scoped feature branches and merges back via pull request after review — at minimum a second team member should look at each PR before merge.

**Branch naming convention:** `feature/<sprint-scope>` for sprint-level work, `feature/<sprint-scope>/<sub-task>` for finer-grained parallel work within a sprint.

```bash
git checkout main
git pull origin main

git checkout -b feature/project-setup                       && git push -u origin feature/project-setup
git checkout main && git checkout -b feature/auth-and-portals                && git push -u origin feature/auth-and-portals
git checkout main && git checkout -b feature/assessment-management           && git push -u origin feature/assessment-management
git checkout main && git checkout -b feature/identity-room-verification      && git push -u origin feature/identity-room-verification
git checkout main && git checkout -b feature/phone-placement-verification    && git push -u origin feature/phone-placement-verification
git checkout main && git checkout -b feature/behavior-monitoring-detection   && git push -u origin feature/behavior-monitoring-detection
git checkout main && git checkout -b feature/browser-audio-monitoring        && git push -u origin feature/browser-audio-monitoring
git checkout main && git checkout -b feature/risk-scoring-engine             && git push -u origin feature/risk-scoring-engine
git checkout main && git checkout -b feature/ai-report-integration           && git push -u origin feature/ai-report-integration
git checkout main && git checkout -b feature/testing-optimization            && git push -u origin feature/testing-optimization
git checkout main && git checkout -b feature/docs-deployment                 && git push -u origin feature/docs-deployment
```

| Branch | Maps to | Covers | Suggested owner(s) |
|---|---|---|---|
| `feature/project-setup` | Sprint 1 | Repo scaffolding, CI, Prisma schema, system design | All |
| `feature/auth-and-portals` | Sprint 2 | JWT auth, registration/login, Company & Candidate portal shells | Hamda |
| `feature/assessment-management` | Sprint 3 | Assessment creation, scheduling, email invites, dashboard, countdown timer | Abdullah, Noor |
| `feature/identity-room-verification` | Sprint 4 | Face/ID verification, room & desk verification | Hamda |
| `feature/phone-placement-verification` | Sprint 4–6 | Phone placement verification flow | Hamda |
| `feature/behavior-monitoring-detection` | Sprint 5 | Head pose, eye gaze, multi-person, object detection | Abdullah |
| `feature/browser-audio-monitoring` | Sprint 6 | Browser monitoring, door monitoring, audio monitoring | Noor |
| `feature/risk-scoring-engine` | Sprint 7–8 | Risk rules, thresholds, rule-based scoring engine | All (shared module) |
| `feature/ai-report-integration` | Sprint 9 | Wiring AI modules into the backend, report generation, risk score APIs | Noor, Hamda |
| `feature/testing-optimization` | Sprint 10 | Test coverage, bug fixes, performance | All |
| `feature/docs-deployment` | Sprint 11 | Final documentation, deployment, presentation prep | All |

**Sub-branch example** for splitting a sprint across two people:

```bash
git checkout -b feature/behavior-monitoring-detection/object-detection feature/behavior-monitoring-detection
git checkout -b feature/behavior-monitoring-detection/head-pose feature/behavior-monitoring-detection
```

**Commit message convention (suggested):** `<type>(<scope>): <short description>`, e.g. `feat(auth): add JWT refresh token endpoint`, `fix(risk-engine): correct tab-switch threshold`, `docs(readme): update sprint plan`.

## 16. Repository Setup Checklist

Per the FYDP GitHub repository requirements:

- [ ] Repository structured with the folder hierarchy in [Section 7](#7-project-structure)
- [ ] `main` branch created, with feature branches per [Section 15](#15-branching-strategy--git-workflow)
- [ ] Meaningful commit history maintained throughout the project
- [ ] This `README.md` included with project description, setup instructions, and execution guidelines
- [ ] Supervisor (Dr Natalia Chaudhary) added as a repository collaborator
- [ ] `fydp.dse@pucit.edu.pk` added as a collaborator (Read or Write access)
- [ ] Repository URL entered in the FYDP Google Sheet under group BSEF23-07's row

## 17. Supervisor & Approval

**Primary Supervisor:** Dr Natalia Chaudhary, Assistant Professor
**Co-supervisor:** *TBD*
**Head of FYDP Coordination Office:** Dr Natalia Chaudhry


