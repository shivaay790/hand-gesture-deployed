import React, { useState } from 'react';
import { Power, ShieldAlert, Gamepad2, Cpu } from 'lucide-react';

const profiles = [
  { id: 'GEOMETRY_DASH', label: 'Geometry Dash (Jump Only)', icon: <Gamepad2 size={18} /> },
  { id: 'FRUIT_NINJA', label: 'Fruit Ninja (Mouse Slice)', icon: <Cpu size={18} /> },
  { id: 'ROBOT', label: 'Robot Telemetry', icon: <Cpu size={18} /> },
];

function ControlPanel({ isActive, onStart, onStop, profile, setProfile, gamePath, setGamePath }) {
  return (
    <div className="glass-dark border border-gray-700/50 backdrop-blur-lg rounded-2xl p-8 shadow-glass">
      <div className="mb-8">
        <h2 className="text-2xl font-bold font-mono text-neon-green mb-1 flex items-center gap-2">
          <Cpu /> CONTROL PANEL
        </h2>
        <p className="text-gray-400 font-mono text-sm">Configure system parameters</p>
      </div>

      <div className="space-y-7">
        {/* Profile Selector */}
        <div>
          <label className="block text-sm font-semibold text-gray-300 mb-3 font-mono">
            ACTIVE PROFILE
          </label>
          <div className="grid gap-3">
            {profiles.map((p) => (
              <label
                key={p.id}
                className={`
                  flex items-center gap-3 p-4 rounded-xl border cursor-pointer transition-all
                  ${profile === p.id ? 'border-neon-green bg-black/50 text-neon-green' : 'border-gray-600 bg-black/30 text-gray-400 hover:border-gray-500'}
                `}
              >
                <input
                  type="radio"
                  name="profile"
                  value={p.id}
                  checked={profile === p.id}
                  onChange={(e) => setProfile(e.target.value)}
                  className="w-4 h-4 accent-neon-green"
                />
                {p.icon}
                <span className="font-mono text-sm">{p.label}</span>
              </label>
            ))}
          </div>
        </div>

        {/* Game Path Input */}
        <div>
          <label className="block text-sm font-semibold text-gray-300 mb-3 font-mono">
            GAME EXECUTABLE PATH
          </label>
          <div className="relative">
            <span className="absolute left-4 top-1/2 -translate-y-1/2 text-gray-500 font-mono text-lg">
              $
            </span>
            <input
              type="text"
              value={gamePath}
              onChange={(e) => setGamePath(e.target.value)}
              placeholder="C:\\Games\\GeometryDash.exe"
              className="w-full bg-black border border-gray-600 rounded-xl px-10 py-4 font-mono text-gray-200 focus:outline-none focus:border-neon-green focus:ring-1 focus:ring-neon-green"
            />
          </div>
        </div>

        {/* Control Buttons */}
        <div className="grid grid-cols-2 gap-4 pt-4">
          <button
            onClick={onStart}
            disabled={isActive}
            className={`
              flex items-center justify-center gap-2 font-bold py-5 rounded-xl font-mono text-lg transition-all
              ${isActive 
                ? 'bg-gray-800 text-gray-600 cursor-not-allowed' 
                : 'bg-black border border-neon-green text-neon-green hover:bg-neon-green/10 shadow-neon-glow-green'}
            `}
          >
            <Power size={24} />
            INITIALIZE SYSTEM
          </button>
          <button
            onClick={onStop}
            disabled={!isActive}
            className={`
              flex items-center justify-center gap-2 font-bold py-5 rounded-xl font-mono text-lg transition-all
              ${!isActive 
                ? 'bg-gray-800 text-gray-600 cursor-not-allowed' 
                : 'bg-black border border-alert-red text-alert-red hover:bg-alert-red/10 shadow-neon-glow-red'}
            `}
          >
            <ShieldAlert size={24} />
            EMERGENCY ABORT
          </button>
        </div>
      </div>
    </div>
  );
}

export default ControlPanel;
