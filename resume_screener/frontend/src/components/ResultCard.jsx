import React from 'react';

function ResultCard({ result }) {
  return (
    <div style={styles.card}>
      <h2>Screening Result</h2>
      <p><strong>Score:</strong> {result.score}</p>
      <p><strong>Feedback:</strong> {result.feedback}</p>
    </div>
  );
}

const styles = {
  card: {
    marginTop: '2rem',
    padding: '1.5rem',
    backgroundColor: 'white',
    borderRadius: '8px',
    boxShadow: '0 2px 10px rgba(0,0,0,0.1)',
    maxWidth: '500px',
    margin: '2rem auto',
  },
};

export default ResultCard;
