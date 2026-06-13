import React, { useEffect, useRef } from 'react';
import { Terminal } from 'lucide-react';

function TelemetryTerminal({ logs }) {
  const terminalRef = useRef(null);

  useEffect(() => {
    if (terminalRef.current) {
      terminalRef.current.scrollTop = terminalRef.current.scrollHeight;
    }
  }, [logs]);

  return (
    <div className="glass-dark border border-gray-700/50 backdrop-blur-lg rounded-2xl p-8 shadow-glass flex flex-col h-full">
      <div className="flex items-center gap-2 mb-5 pb-4 border-b border-gray-700/50">
        <Terminal size={20} className="text-neon-green" />
        <h2 className="text-xl font-bold font-mono text-neon-green">TELEMETRY TERMINAL</h2>
      </div>

      <div
        ref={terminalRef}
        className="flex-1 bg-black/80 rounded-xl p-5 overflow-y-auto font-mono text-sm"
      >
        {logs.map((log, index) => (
          <div key={index} className="text-neon-green mb-1">
            {log}
          </div>
        ))}
      </div>
    </div>
  );
}

export default TelemetryTerminal;
