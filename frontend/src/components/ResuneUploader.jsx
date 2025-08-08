// Example: src/components/ResumeUploader.js
import React, { useState } from 'react';

function ResumeUploader() {
  const [file, setFile] = useState(null);

  const handleFileUpload = async () => {
    const formData = new FormData();
    formData.append('resume', file);

    try {
      const res = await fetch('http://localhost:8000/api/upload_resume/', {
        method: 'POST',
        body: formData,
      });
      if (!res.ok) {
        throw new Error("Failed to upload");
      }

      const data = await res.json();
      console.log('Server Response:', data);
    } catch (err) {
      console.error('Fetch error:', err);
      alert('Failed to connect to backend.');
    }
  };

  return (
    <div>
      <form onSubmit={handleUpload}>
        <input type="file" onChange={(e) => setFile(e.target.files[0])} />
        <button type="submit">Upload Resume</button>
      </form>

      {response && (
        <div>
          <h3>Response:</h3>
          <pre>{JSON.stringify(response, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default ResumeUploader;
