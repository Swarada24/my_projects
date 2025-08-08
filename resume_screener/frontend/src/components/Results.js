import React from 'react';
import { Card, CardContent, Typography } from '@mui/material';

function Results({ results }) {
  if (!results) return null;

  return (
    <Card sx={{ mt: 4 }}>
      <CardContent>
        <Typography variant="h6">Screening Results:</Typography>
        <Typography variant="body1">{results.summary}</Typography>
      </CardContent>
    </Card>
  );
}

export default Results;
