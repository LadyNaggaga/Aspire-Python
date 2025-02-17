# Vue + FastAPI + .NET Aspire Chat Application

A modern chat application built with Vue.js, FastAPI, and .NET Aspire, supporting both local development with Ollama and production deployment with Azure OpenAI.

## Prerequisites

- Node.js 20+
- Python 3.11+
- .NET 9.0 SDK
- Docker
- Ollama (for local development)
- Azure OpenAI Service (for production)

## Project Structure

```
├── aspire/             # .NET Aspire orchestration
├── backend/            # Python FastAPI backend
└── frontend/          # Vue.js frontend
```

## Setup

1. Install .NET Aspire workload:
```bash
dotnet workload install aspire
```

2. Install backend dependencies:
```bash
cd backend
pip install -r requirements.txt
```

3. Install frontend dependencies:
```bash
npm install
```

4. Configure environment variables:
```bash
cp backend/.env.example backend/.env
```

Edit `.env` file with your configuration:
- For local development: Use `ENVIRONMENT=local`
- For production: Set Azure OpenAI credentials

## Development

### Local Development with Ollama

1. Start Ollama and pull the Mistral model:
```bash
ollama pull mistral
```

2. Start the application with Aspire:
```bash
cd aspire
dotnet run
```

This will start:
- Frontend at http://localhost:5173
- Backend at http://localhost:8000
- Aspire dashboard at http://localhost:15888

### Production Deployment

1. Update environment variables for Azure OpenAI
2. Build and deploy using Docker containers

## Features

- Real-time chat interface
- Local development using Ollama
- Production deployment with Azure OpenAI
- .NET Aspire orchestration
- Health monitoring and logging
- Service discovery and networking

## License

MIT
