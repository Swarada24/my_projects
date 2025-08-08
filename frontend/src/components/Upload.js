import React, { useState } from 'react';
import { Button, Box, Typography } from '@mui/material';

function Upload() {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => setFile(e.target.files[0]);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('resume', file);

    const res = await fetch('http://localhost:5000/api/upload_resume/', {
      method: 'POST',
      body: formData
    });

    const data = await res.json();
    console.log(data); // handle results
  };

  return (
    <Box sx={{ mt: 3 }}>
      <input type="file" accept=".pdf,.docx" onChange={handleFileChange} />
      <Button variant="contained" sx={{ ml: 2 }} onClick={handleUpload} disabled={!file}>
        Upload Resume
      </Button>
    </Box>
  );
}

export default Upload;
