import React from 'react';
import Upload from './components/Upload';
import Results from './components/Results';
import { Container, Typography } from '@mui/material';

function App() {
  return (
    <Container maxWidth="md" sx={{ mt: 4 }}>
      <Typography variant="h3" gutterBottom align="center">
        Resume Screener
      </Typography>
      <Upload />
      <Results />
    </Container>
  );
}

export default App;
