import React, { useState, useEffect } from 'react';
import { Zap } from 'lucide-react';
import ControlPanel from './components/ControlPanel';
import TelemetryTerminal from './components/TelemetryTerminal';
import { api } from './services/api';

function App() {
  const [isActive, setIsActive] = useState(false);
  const [logs, setLogs] = useState([]);
  const [profile, setProfile] = useState('GEOMETRY_DASH');
  const [gamePath, setGamePath] = useState('');

  const addLog = (message) => {
    const timestamp = new Date().toLocaleTimeString('en-US', { hour12: false });
    setLogs((prev) => [...prev, `[${timestamp}] ${message}`]);
  };

  useEffect(() => {
    addLog('Gesture Control Matrix initialized');
    addLog('Awaiting system commands...');
  }, []);

  const handleStart = async () => {
    addLog('Sending INITIALIZE command to backend...');
    const result = await api.startGame(profile, gamePath);
    
    if (result.success) {
      setIsActive(true);
      addLog(`SUCCESS: ${result.data.message}`);
    } else {
      addLog(`ERROR: ${result.error}`);
    }
  };

  const handleStop = async () => {
    addLog('Sending ABORT command to backend...');
    const result = await api.stopGame();
    
    if (result.success) {
      setIsActive(false);
      addLog(`SUCCESS: ${result.data.message}`);
      addLog('Engine offline');
    } else {
      addLog(`ERROR: ${result.error}`);
    }
  };

  return (
    <div className="min-h-screen bg-matrix-black p-8">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <header className="mb-10 text-center">
          <h1 className="text-6xl font-extrabold font-mono text-white mb-3 flex items-center justify-center gap-4">
            <Zap size={48} className="text-neon-green animate-pulse" />
            GESTURE CONTROL OVERRIDE
          </h1>
          <p className="text-gray-400 font-mono text-lg uppercase tracking-widest">
            Computer Vision Interface v1.0.0
          </p>
        </header>

        {/* Main Content Grid */}
        <main className="grid grid-cols-1 lg:grid-cols-2 gap-8 items-stretch">
          <ControlPanel
            isActive={isActive}
            onStart={handleStart}
            onStop={handleStop}
            profile={profile}
            setProfile={setProfile}
            gamePath={gamePath}
            setGamePath={setGamePath}
          />
          <TelemetryTerminal logs={logs} />
        </main>
      </div>
    </div>
  );
}

export default App;
