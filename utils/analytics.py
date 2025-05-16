import pandas as pd
import numpy as np
import plotly.express as px # type: ignore

def calculate_progress(student_data):
    performance = student_data.get('performance', {})
    progress = {}
    
    for topic, answers in performance.items():
        scores = []
        for answer in answers:
            # Extract score from feedback (simple implementation)
            feedback = answer['feedback']
            try:
                score = int(feedback.split("Score: ")[1].split("/")[0])
                scores.append(score)
            except:
                scores.append(50)  # Default if parsing fails
        
        if scores:
            progress[topic] = {
                'attempts': len(scores),
                'average_score': np.mean(scores),
                'highest_score': max(scores),
                'lowest_score': min(scores),
                'improvement': scores[-1] - scores[0] if len(scores) > 1 else 0
            }
    
    return progress

def plot_performance(student_data):
    performance = student_data.get('performance', {})
    
    # Prepare data for plotting
    plot_data = []
    for topic, answers in performance.items():
        for i, answer in enumerate(answers):
            try:
                score = int(answer['feedback'].split("Score: ")[1].split("/")[0])
                plot_data.append({
                    'Topic': topic,
                    'Attempt': i+1,
                    'Score': score
                })
            except:
                continue
    
    if not plot_data:
        # Return empty figure if no data
        return px.line(title="No performance data yet")
    
    df = pd.DataFrame(plot_data)
    fig = px.line(
        df, 
        x="Attempt", 
        y="Score", 
        color="Topic",
        title="Your Performance Over Time",
        markers=True
    )
    fig.update_layout(yaxis_range=[0, 100])
    return fig