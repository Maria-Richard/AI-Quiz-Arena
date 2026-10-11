import random

import streamlit as st



st.set_page_config(page_title="AI Game Arena", page_icon="🤖", layout="wide")

st.markdown("""

<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600;700&family=Space+Grotesk:wght@500;700&display=swap');

html,body,[class*="css"]{font-family:'DM Sans',sans-serif}

.stApp{background:radial-gradient(circle at 10% 5%,#202a56 0,transparent 30%),radial-gradient(circle at 90% 10%,#103b43 0,transparent 25%),#0b1020;color:#eef2ff}

h1,h2,h3{font-family:'Space Grotesk',sans-serif;color:#f6f8ff}

div[data-testid="stMetric"]{background:#ffffff0d;border:1px solid #ffffff1c;padding:12px;border-radius:15px}

div.stButton>button{border-radius:12px;font-weight:700;min-height:2.6rem}

.arena{padding:28px;border-radius:22px;background:linear-gradient(120deg,#526dff40,#00cfbe18);border:1px solid #9baeff40;margin-bottom:18px}

.muted{color:#b8c4e4}.pill{display:inline-block;padding:5px 10px;margin:3px;border-radius:99px;background:#6f83ff26;border:1px solid #8b9cff40;font-size:.8rem}

</style>

""", unsafe_allow_html=True)



def Q(t, d, typ, question, answer, explanation, hint, options=None, pairs=None, scenario=False, search=False, aliases=None):

    return dict(topic=t,difficulty=d,type=typ,question=question,answer=answer,explanation=explanation,hint=hint,

                options=(options if options is not None else ([True, False] if typ == TF else None)),
                pairs=(pairs if pairs is not None else (answer if typ == MATCH else None)),
                scenario=scenario,search=search,aliases=aliases or [])



MCQ="MCQ"; TF="True / False"; AR="Assertion–Reasoning"; MATCH="Matching"; FILL="Fill in the Blanks"

AR_OPTIONS=["A and R are true, and R correctly explains A","A and R are true, but R does not correctly explain A","A is true, but R is false","A is false, but R is true"]

QUESTIONS=[

# 10 MCQs

Q("Foundation of AI","Easy",MCQ,"Which statement best describes Artificial Intelligence?",0,"AI builds systems that perform tasks associated with intelligent behavior.","Think reasoning, learning, perception and decisions.",["A system that only stores data","The study of systems performing tasks associated with intelligent behavior","A computer always connected to the internet","Any spreadsheet"]),

Q("Background of AI","Easy",MCQ,"The 1956 Dartmouth workshop is associated with:",1,"The workshop helped establish AI as a named research field.","It was in the 1950s.",["The first web browser","The early establishment of AI as a field","The smartphone","The first search engine"]),

Q("Turing Test","Medium",MCQ,"In the classic Turing Test, a judge tries to:",1,"The judge considers whether machine conversation can be distinguished from human conversation.","It tests conversational behavior.",["Measure processing speed","Distinguish a machine's written conversation from a human's","Test a robot's strength","Check program formatting"]),

Q("AI Applications","Easy",MCQ,"A hospital AI flags possible abnormalities in X-rays for a clinician to review. This is:",0,"AI can assist medical-image analysis; clinicians make care decisions.","It analyses healthcare images.",["Medical image analysis","File compression only","Operating-system scheduling only","Manual data entry"],scenario=True),

Q("Rational Agents","Medium",MCQ,"A navigation app compares traffic and road conditions before recommending a route. This is an example of a rational agent trying to:",0,"The app uses available information to choose the route expected to perform best according to its objective.","Think about its performance measure.",["Maximize expected performance","Repeat the same route always","Use the most memory","Avoid sensing"],scenario=True),

Q("Agents and Environments","Easy",MCQ,"A smart thermostat reads the room temperature before switching the heating on or off. The temperature reading is a:",1,"A percept is sensory input received by an agent at a particular time.","It is the information the device senses.",["The source code","Percept received through a sensor","Always a reward","An actuator"],scenario=True),

Q("Nature of Environments","Medium",MCQ,"Chess with visible board state and fixed rules is generally:",1,"Chess is discrete and fully observable in its standard form.","The board has distinct squares.",["Partially observable and continuous","Fully observable and discrete","Only continuous","Episodic with no interaction"]),

Q("Problem Spaces","Medium",MCQ,"A goal test determines:",0,"It checks whether the current state satisfies the goal condition.","It checks success.",["Whether a state satisfies the goal","Available RAM","Code formatting","Search-tree colours"]),

Q("Uninformed Search","Medium",MCQ,"Which method expands the shallowest unexpanded node first?",1,"BFS expands level by level, usually with a FIFO queue.","One depth level at a time.",["DFS","BFS","Hill Climbing","Greedy Best-First"],search=True),

Q("Heuristic Search","Medium",MCQ,"A heuristic h(n) usually estimates:",0,"A heuristic estimates remaining distance or cost to a goal.","It is an estimate of the goal distance.",["Remaining cost/distance to a goal","Every future state exactly","Program length","Screen resolution"],search=True),

# 10 true false

Q("Foundation of AI","Easy",TF,"AI includes reasoning, learning, perception and language processing.",True,"These are common AI research areas.","Think of different intelligent capabilities."),

Q("Turing Test","Medium",TF,"Passing a Turing Test proves that a machine is conscious.",False,"The test evaluates observable behavior, not consciousness.","Behavioral indistinguishability does not prove inner experience."),

Q("Rational Agents","Medium",TF,"An agent's percept history can influence its action choice.",True,"Agent behavior can depend on percept history and knowledge.","What information can it use?"),

Q("Good Behaviour","Easy",TF,"A rational agent must know the future with certainty.",False,"Rationality is based on expected performance; omniscience is not required.","Rationality is not omniscience."),

Q("Nature of Environments","Medium",TF,"In a simple warehouse simulation, a robot's move to an unblocked adjacent cell always produces the same next position. This transition is deterministic.",True,"In a deterministic environment, the current state and chosen action determine the next state.","Does the same action from the same state always give the same result?",scenario=True),

Q("Production Systems","Medium",TF,"Production systems can represent knowledge with condition–action rules.",True,"Rules often take an IF condition THEN action form.","Think IF–THEN."),

Q("BFS","Medium",TF,"BFS commonly uses a last-in, first-out stack.",False,"BFS usually uses a FIFO queue; DFS may use a stack.","FIFO differs from LIFO.",search=True),

Q("DFS","Medium",TF,"DFS may explore deeply along a branch before backtracking.",True,"DFS prioritizes depth before alternatives.","What does depth-first mean?",search=True),

Q("Hill Climbing","Medium",TF,"Basic hill climbing can become stuck at a local maximum or plateau.",True,"Local evaluations do not guarantee a global optimum.","A locally best state may not be globally best."),

Q("Constraint Satisfaction","Easy",TF,"A CSP is described by variables, domains and constraints.",True,"These are the standard components of a CSP.","Remember the three components."),

# 10 assertion reason

Q("AI Applications","Medium",AR,"Assertion (A): AI can help clinicians identify patterns in medical images.\n\nReason (R): Pattern-recognition methods can identify image features associated with categories.",0,"Both statements are true, and pattern recognition explains the application.","How does pattern recognition support image analysis?",options=AR_OPTIONS,scenario=True),

Q("Turing Test","Medium",AR,"Assertion (A): The Turing Test involves interaction with a human judge.\n\nReason (R): The judge considers whether machine conversation can be distinguished from human conversation.",0,"Both are true; the reason describes the test's basis.","What does the judge try to distinguish?",options=AR_OPTIONS),

Q("Rational Agents","Medium",AR,"Assertion (A): A delivery robot may choose a longer road if it is expected to reach the customer sooner.\n\nReason (R): A rational agent selects actions based on expected performance according to its performance measure.",0,"Both are true, and expected performance explains why the robot may prefer the longer but faster route.","Focus on the goal the robot is trying to achieve.",options=AR_OPTIONS,scenario=True),

Q("Nature of Environments","Medium",AR,"Assertion (A): A warehouse robot may have difficulty navigating when its sensors cannot detect every obstacle.\n\nReason (R): In a partially observable environment, the agent does not receive complete information about the current state.",0,"Both statements are true, and incomplete sensor information explains the robot's difficulty.","Think about what the robot can and cannot sense.",options=AR_OPTIONS,scenario=True),

Q("Problem Spaces","Medium",AR,"Assertion (A): A search problem includes an initial state and a goal test.\n\nReason (R): These specify where search starts and how success is recognized.",0,"Both are true and the reason explains these components.","Think start and success conditions.",options=AR_OPTIONS),

Q("Production Systems","Medium",AR,"Assertion (A): Production systems apply rules to a current situation.\n\nReason (R): Rules are often written as condition–action pairs.",0,"Both are true and the reason describes production-rule structure.","Think of an IF–THEN rule.",options=AR_OPTIONS),

Q("BFS","Medium",AR,"Assertion (A): BFS finds a shortest path when every step has equal cost, under standard graph-search assumptions.\n\nReason (R): BFS expands nodes in nondecreasing depth order.",0,"Both are true; depth-order expansion gives shortest paths for equal step costs.","How does BFS order nodes?",options=AR_OPTIONS,search=True),

Q("DFS","Medium",AR,"Assertion (A): DFS is not generally optimal for finding a shallowest solution.\n\nReason (R): DFS may follow a deep branch before exploring a shallower alternative.",0,"Both are true; the exploration order explains the limitation.","Consider which branch DFS follows first.",options=AR_OPTIONS,search=True),

Q("Hill Climbing","Medium",AR,"Assertion (A): Hill climbing may fail to reach a global optimum.\n\nReason (R): It often chooses a locally improving neighbor without searching the whole space.",0,"Both are true; local choices can lead to local optima.","Local improvement does not guarantee a global optimum.",options=AR_OPTIONS),

Q("Constraint Satisfaction","Easy",AR,"Assertion (A): A CSP solution must satisfy every constraint.\n\nReason (R): An assignment violating a constraint is not a valid solution.",0,"Both are true and the reason explains the solution requirement.","All constraints must hold.",options=AR_OPTIONS),

# 10 matching

Q("AI Foundations","Easy",MATCH,"Match each AI term to its description.",{"Turing Test":"Conversational test of machine behavior","Perception":"Interpreting sensory input","Learning":"Improving behavior from experience/data","Reasoning":"Drawing conclusions from information"},"The matches distinguish common AI concepts.","Match each term to its role."),

Q("Intelligent Agents","Medium",MATCH,"A smart-home assistant uses the following components. Match each component to its role.",{"Sensors":"Receive percepts","Actuators":"Carry out actions","Agent function":"Maps percept history to actions","Performance measure":"Defines success"},"Sensors receive information, actuators carry out actions, the agent function selects actions, and the performance measure evaluates success.","Input, output, decision, evaluation.",scenario=True),

Q("Rational Agents","Medium",MATCH,"Match each term to its meaning.",{"Rationality":"Choosing actions expected to maximize performance","Omniscience":"Knowing the actual outcome in advance","Autonomy":"Using experience as well as built-in knowledge","Percept":"Input received from sensors"},"Rationality does not imply omniscience.","Rational and omniscient are not synonyms."),

Q("Nature of Environments","Medium",MATCH,"Match the environment property to its description.",{"Fully observable":"Relevant state is accessible","Partially observable":"State information is incomplete","Deterministic":"Action has a predictable outcome","Stochastic":"Outcome involves uncertainty"},"These terms describe observability and outcome uncertainty.","Visibility differs from uncertainty."),

Q("Problem Spaces","Medium",MATCH,"Match each problem component to its role.",{"Initial state":"Where search begins","Goal test":"Checks whether goal reached","Actions":"Available transitions","Path cost":"Accumulated cost of a path"},"These are standard search-problem elements.","Start, test, moves and cost."),

Q("Uninformed Search","Medium",MATCH,"Match each search term to its description.",{"BFS":"Expands shallowest nodes first","DFS":"Explores deeply before backtracking","Iterative deepening":"Repeats depth-limited search with increasing limits","Queue":"Typical BFS frontier structure"},"The methods differ in node ordering and frontier handling.","Recall the depth strategy.",search=True),

Q("Heuristic Search","Medium",MATCH,"Match each heuristic term to its role.",{"h(n)":"Estimates remaining cost to goal","Greedy Best-First":"Selects using h(n)","Hill climbing":"Moves toward a better neighbor","Local maximum":"Locally best but not globally best"},"These terms describe heuristic guidance and a common limitation.","Estimate versus local neighbor quality.",search=True),

Q("Constraint Satisfaction","Easy",MATCH,"Match each CSP element to its meaning.",{"Variable":"Item that needs a value","Domain":"Available values","Constraint":"Restriction on assignments","Consistent assignment":"Violates no constraints"},"CSPs use variables, domains and constraints.","A domain lists possible values."),

Q("Means-End Analysis","Medium",MATCH,"Match each means–end term to its role.",{"Current state":"Situation now","Goal state":"Desired target","Difference":"Gap between current and goal","Operator":"Action that can reduce a difference"},"Means–end analysis compares current and goal states and chooses operators.","Compare present with target."),

Q("Search Design","Hard",MATCH,"Match each search concept to its description.",{"Repeated state":"State reached again by another path","Frontier":"Generated nodes awaiting expansion","Explored set":"States already processed","Branching factor":"Average number of successors"},"Search efficiency depends on managing repeated states and pending/processed nodes.","Pending, processed, successors.",search=True),

# 10 fill blanks

Q("Foundation of AI","Easy",FILL,"The test proposed by Alan Turing is commonly called the ______ Test.","Turing","It is known as the Turing Test.","The missing word is the scientist's surname."),

Q("AI Applications","Easy",FILL,"Converting spoken language into text is called ______ recognition.","speech","Speech recognition processes spoken audio.","It processes spoken audio.",scenario=True,aliases=["speech"]),

Q("Rational Agents","Medium",FILL,"An agent's behavior is evaluated using a ______ measure.","performance","A performance measure defines success.","It defines success.",aliases=["performance"]),

Q("Agents and Environments","Easy",FILL,"A robotic vacuum cleaner detects walls and furniture using devices that collect information about its surroundings. These devices are called ______.","sensors","Sensors provide percepts and help an agent detect features of its environment.","They are the input side of the agent.",scenario=True,aliases=["sensor"]),

Q("Production Systems","Medium",FILL,"A production rule is often written as IF condition, THEN ______.","action","Production systems use condition–action rules.","What happens when the condition holds?",aliases=["action"]),

Q("Uninformed Search","Medium",FILL,"BFS commonly stores its frontier in a first-in, first-out ______.","queue","A FIFO queue supports level-by-level BFS.","First in, first out.",search=True,aliases=["queue"]),

Q("Uninformed Search","Medium",FILL,"DFS can be implemented using a stack or ______.","recursion","Recursive calls can implement depth-first traversal.","A function calls itself.",search=True,aliases=["recursion","recursive calls"]),

Q("Heuristic Search","Medium",FILL,"In heuristic search, h(n) estimates remaining cost from n to the ______.","goal","A heuristic estimates the distance/cost to the goal.","The desired destination.",search=True,aliases=["goal","goal state"]),

Q("Constraint Satisfaction","Easy",FILL,"A CSP consists of variables, domains and ______.","constraints","Constraints restrict valid assignments.","They restrict combinations.",aliases=["constraints"]),

Q("Means-End Analysis","Medium",FILL,"Means–end analysis reduces the difference between the current state and the ______ state.","goal","It selects operators to reduce the current-to-goal difference.","The desired target.",aliases=["goal","goal state"]),

]



EXPECTED={MCQ:10,TF:10,AR:10,MATCH:10,FILL:10}

counts={t:sum(q["type"]==t for q in QUESTIONS) for t in EXPECTED}

if len(QUESTIONS)!=50 or counts!=EXPECTED:

    st.error(f"Question bank validation failed: {len(QUESTIONS)} questions; {counts}")

    st.stop()



MISSION_KEYWORDS={

"AI Foundations":["Foundation","Background","Turing","AI Applications"],

"Agents & Environments":["Rational","Agent","Behaviour","Environment","Intelligent"],

"Problem Solving":["Problem","Production","Search Design"],

"Uninformed Search":["Uninformed","BFS","DFS","Iterative"],

"Heuristic Search":["Heuristic","Hill Climbing","Constraint","Means-End","Search Design"]

}

def accepted(q, mission, difficulty):

    return (mission=="All Topics" or any(k.lower() in q["topic"].lower() for k in MISSION_KEYWORDS[mission])) and (difficulty=="All levels" or q["difficulty"]==difficulty)

def correct(q, ans):
    if q["type"] == MATCH:
        return isinstance(ans, dict) and all(ans.get(k) == v for k, v in q["answer"].items())

    if q["type"] == FILL:
        accepted_answers = [q["answer"].lower()] + [x.lower() for x in q["aliases"]]
        return str(ans or "").strip().lower() in accepted_answers

    if q["type"] in [MCQ, AR]:
        return ans == q["options"][q["answer"]]

    return ans == q["answer"]

def navigate():
    """Only change screens when the sidebar navigation is changed."""
    choice = st.session_state.nav
    if choice == "Home":
        st.session_state.screen = "home"
    elif choice == "Question Bank":
        st.session_state.screen = "bank"
    elif choice == "Leaderboard / Results":
        st.session_state.screen = "results"
    elif choice == "Play Quiz" and st.session_state.screen not in ["quiz", "result"]:
        st.session_state.screen = "setup"


def start():

    pool=[q for q in QUESTIONS if accepted(q,st.session_state.mission,st.session_state.difficulty)]

    random.shuffle(pool)

    if not pool:
        st.session_state.quiz = []
        st.session_state.i = 0
        st.session_state.answers = {}
        st.session_state.submitted = set()
        st.session_state.hints = set()
        st.session_state.screen = "quiz"
        st.session_state.run_id += 1
        return

    if st.session_state.mode=="Quick Challenge (10 random questions)": pool=pool[:min(10,len(pool))]

    st.session_state.quiz=pool; st.session_state.i=0; st.session_state.answers={}; st.session_state.submitted=set()

    st.session_state.hints=set(); st.session_state.screen="quiz"; st.session_state.run_id+=1



for k,v in {"screen":"home","player":"Player One","mode":"Quick Challenge (10 random questions)","mission":"All Topics","difficulty":"All levels","quiz":[],"i":0,"answers":{},"submitted":set(),"hints":set(),"xp":0,"best":0,"history":[],"run_id":0}.items():

    if k not in st.session_state: st.session_state[k]=v



with st.sidebar:

    st.markdown("## 🤖 AI GAME ARENA")

    if "nav" not in st.session_state:
        st.session_state.nav = "Home"
    st.radio(
        "NAVIGATION",
        ["Home", "Play Quiz", "Question Bank", "Leaderboard / Results"],
        key="nav",
        on_change=navigate,
    )

    st.divider()

    st.session_state.player=st.text_input("Player name",st.session_state.player,max_chars=30)

    st.metric("⭐ Total XP",st.session_state.xp); st.metric("🏆 Best score",st.session_state.best)


if st.session_state.screen=="home":

    st.markdown('<div class="arena"><h1 style="font-size:3rem">Enter the AI Game Arena 🤖</h1><p class="muted">Test your AI knowledge, solve search challenges, earn XP, and master intelligent agents and problem solving.</p><span class="pill">50 questions</span><span class="pill">5 question formats</span><span class="pill">Missions & XP</span><span class="pill">Instant feedback</span></div>',unsafe_allow_html=True)

    a,b,c,d=st.columns(4); a.metric("Question bank","50"); b.metric("Question types","5"); c.metric("Scenario questions",sum(q["scenario"] for q in QUESTIONS)); d.metric("Search problems",sum(q["search"] for q in QUESTIONS))

    st.markdown("### 🎮 Choose your challenge")

    x,y=st.columns(2)

    with x:

        st.markdown("#### ⚡ Quick Challenge\nRandomly choose 10 questions for a short practice run.")

        if st.button("Start 10-question challenge →",type="primary",use_container_width=True):

            st.session_state.mode="Quick Challenge (10 random questions)"; st.session_state.mission="All Topics"; st.session_state.difficulty="All levels"; start(); st.rerun()

    with y:

        st.markdown("#### 🧠 Full Arena Run\nAttempt all 50 questions with feedback and answer review.")

        if st.button("Start full 50-question run →",use_container_width=True):

            st.session_state.mode="Full Arena Run (50 questions)"; st.session_state.mission="All Topics"; st.session_state.difficulty="All levels"; start(); st.rerun()

    st.markdown("### 🗺️ Missions")

    cols=st.columns(5)

    desc=["AI basics, applications & Turing Test","Rationality and environment types","States, production rules & search design","BFS, DFS & iterative deepening","Hill climbing, heuristics, CSP & means–end"]

    for col,(mission,description) in zip(cols,zip(MISSION_KEYWORDS,desc)):

        with col:

            st.markdown(f"**{mission}**\n\n<p class='muted'>{description}</p>",unsafe_allow_html=True)

            if st.button("Play mission",key="mission_"+mission,use_container_width=True):

                st.session_state.mission=mission; st.session_state.mode="Quick Challenge (10 random questions)"; st.session_state.difficulty="All levels"; start(); st.rerun()

    st.info("Correct answers earn 10 XP. Using a hint reduces a correct answer's reward to 5 XP.")

elif st.session_state.screen=="setup":

    st.title("🎮 Set up your challenge")

    st.session_state.mode=st.radio("Game mode",["Quick Challenge (10 random questions)","Full Arena Run (50 questions)"])

    st.session_state.mission=st.selectbox("Mission / topic",["All Topics"]+list(MISSION_KEYWORDS))

    st.session_state.difficulty=st.selectbox("Difficulty",["All levels","Easy","Medium","Hard"])

    if st.button("Start challenge",type="primary"): start(); st.rerun()

elif st.session_state.screen=="quiz":

    qs=st.session_state.quiz; i=st.session_state.i

    if not qs: st.warning("No active quiz. Return Home to start.")

    elif i>=len(qs): st.session_state.screen="result"; st.rerun()

    else:

        q=qs[i]; st.markdown(f"### Question {i+1} of {len(qs)}"); st.progress((i+1)/len(qs))

        a,b,c=st.columns(3); a.metric("⭐ XP",st.session_state.xp); b.metric("Correct so far",sum(correct(qs[j],st.session_state.answers.get(j)) for j in st.session_state.submitted)); c.metric("Hints used",len(st.session_state.hints))

        st.markdown(f'<span class="pill">{q["type"]}</span><span class="pill">{q["topic"]}</span><span class="pill">{q["difficulty"]}</span>',unsafe_allow_html=True)

        st.markdown("---"); st.markdown("#### "+q["question"])

        if st.button("💡 Use hint / lifeline",key=f"hint_{st.session_state.run_id}_{i}"): st.session_state.hints.add(i)

        if i in st.session_state.hints: st.info("Hint: "+q["hint"])

        if q["type"]==MATCH:

            ans={}

            for j,(term,desc) in enumerate(q["pairs"].items()):

                opts=list(q["pairs"].values()); previous=st.session_state.answers.get(i,{}).get(term,opts[0])

                ans[term]=st.selectbox(term,opts,index=opts.index(previous) if previous in opts else 0,key=f"match_{st.session_state.run_id}_{i}_{j}")

            st.session_state.answers[i]=ans

        elif q["type"]==FILL:

            st.session_state.answers[i]=st.text_input("Your answer",value=st.session_state.answers.get(i,""),key=f"fill_{st.session_state.run_id}_{i}",placeholder="Type your answer...")

        else:

            opts=q["options"]; prev=st.session_state.answers.get(i); ix=opts.index(prev) if prev in opts else None

            st.session_state.answers[i]=st.radio("Choose your answer",opts,index=ix,key=f"answer_{st.session_state.run_id}_{i}")

        if i not in st.session_state.submitted:

            if st.button("Submit answer",type="primary",key=f"submit_{st.session_state.run_id}_{i}"):

                ans=st.session_state.answers.get(i)

                if ans is None or ans=="": st.warning("Please answer before submitting.")

                else:

                    st.session_state.submitted.add(i)

                    if correct(q,ans): st.session_state.xp+=5 if i in st.session_state.hints else 10

                    st.rerun()

        else:

            isright=correct(q,st.session_state.answers.get(i))

            if isright: st.success("✅ Correct! "+("5 XP earned because you used a hint." if i in st.session_state.hints else "10 XP earned."))

            else: st.error("❌ Not quite. Review the correct answer below.")

            if q["type"]==MATCH:

                st.markdown("**Correct matches:**")

                for term,desc in q["answer"].items(): st.write(f"- **{term}** → {desc}")

            elif q["type"]==FILL: st.write("**Accepted answer:** "+q["answer"])

            elif q["type"]==TF: st.write("**Correct answer:** "+str(q["answer"]))

            else: st.write("**Correct answer:** "+q["options"][q["answer"]])

            st.info(q["explanation"])

            p,n=st.columns(2)

            with p:

                if st.button("← Previous",disabled=i==0,key=f"prev_{st.session_state.run_id}_{i}"): st.session_state.i-=1; st.rerun()

            with n:

                if st.button("Finish quiz →" if i==len(qs)-1 else "Next question →",type="primary",key=f"next_{st.session_state.run_id}_{i}"):

                    st.session_state.i+=1

                    if st.session_state.i>=len(qs):

                        score=sum(correct(qs[j],st.session_state.answers.get(j)) for j in st.session_state.submitted)

                        st.session_state.best=max(st.session_state.best,score)

                        st.session_state.history.append({"Player":st.session_state.player or "Player","Score":f"{score}/{len(qs)}","Accuracy":f"{round(100*score/len(qs))}%","Mode":st.session_state.mode,"Mission":st.session_state.mission})

                        st.session_state.screen="result"

                    st.rerun()

elif st.session_state.screen=="result":

    qs=st.session_state.quiz; total=len(qs); score=sum(correct(qs[j],st.session_state.answers.get(j)) for j in st.session_state.submitted); pct=round(score*100/total) if total else 0

    st.markdown('<div class="arena"><h1>Challenge complete 🏆</h1><p class="muted">Every attempt strengthens your AI problem-solving skills.</p></div>',unsafe_allow_html=True)

    a,b,c=st.columns(3); a.metric("Correct answers",f"{score}/{total}"); b.metric("Accuracy",f"{pct}%"); c.metric("Total XP",st.session_state.xp)

    st.success("Excellent work!" if pct>=80 else "Good progress—review explanations and practise again." if pct>=50 else "Keep practising; review the missed questions.")

    st.markdown("### Answer review")

    for i,q in enumerate(qs):

        ans=st.session_state.answers.get(i); right=correct(q,ans) if i in st.session_state.submitted else False

        with st.expander(f"{'✅' if right else '❌'} Q{i+1}. {q['topic']} — {q['type']}"):

            st.markdown(q["question"])

            if q["type"]==MATCH:

                for term,desc in q["answer"].items(): st.write(f"- **{term}** → {desc}")

            elif q["type"]==FILL: st.write("**Correct answer:** "+q["answer"]); st.write("**Your answer:** "+str(ans or "(no answer)"))

            elif q["type"]==TF: st.write("**Correct answer:** "+str(q["answer"])); st.write("**Your answer:** "+str(ans))

            else: st.write("**Correct answer:** "+q["options"][q["answer"]]); st.write("**Your answer:** "+str(ans))

            st.caption(q["explanation"])

    if st.button("Play another challenge",type="primary"): st.session_state.screen="home"; st.rerun()

elif st.session_state.screen=="bank":

    st.title("📚 Question Bank"); st.caption("All 50 questions, answers and explanations for study/submission.")

    typ=st.selectbox("Question type",["All types"]+list(EXPECTED)); topic=st.selectbox("Topic",["All topics"]+sorted({q["topic"] for q in QUESTIONS}))

    bank=[q for q in QUESTIONS if (typ=="All types" or q["type"]==typ) and (topic=="All topics" or q["topic"]==topic)]

    st.write(f"Showing {len(bank)} of 50 questions")

    lines=[]

    for i,q in enumerate(bank,1):

        with st.expander(f"{i}. [{q['type']}] {q['topic']} — {q['difficulty']}"):

            st.markdown(q["question"])

            if q["type"]==MATCH:

                for term,desc in q["answer"].items(): st.write(f"- **{term}** → {desc}")

            elif q["type"]==FILL: st.write("**Answer:** "+q["answer"])

            elif q["type"]==TF: st.write("**Answer:** "+str(q["answer"]))

            else: st.write("**Answer:** "+q["options"][q["answer"]])

            st.caption(q["explanation"])

        answer=(str(q["answer"]) if q["type"] in [TF,FILL] else "; ".join(f"{k} -> {v}" for k,v in q["answer"].items()) if q["type"]==MATCH else q["options"][q["answer"]])

        lines.append(f"{i}. [{q['type']}] {q['topic']}\n{q['question']}\nAnswer: {answer}\nExplanation: {q['explanation']}")

    st.download_button("Download question bank (.txt)", "\n\n".join(lines), "AI_Game_Arena_Question_Bank.txt", "text/plain")

elif st.session_state.screen=="results":

    st.title("🏆 Leaderboard & Results")

    if st.session_state.history: st.dataframe(st.session_state.history,use_container_width=True,hide_index=True)

    else: st.info("No completed runs yet. Finish a challenge to appear here.")

    if st.button("Return to Home",type="primary"): st.session_state.screen="home"; st.rerun()



st.markdown("---")

st.caption("AI Game Arena • DSC401-6 Artificial Intelligence • Units I & II • Built with Python and Streamlit")
