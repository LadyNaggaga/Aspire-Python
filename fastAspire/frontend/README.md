# Vue + FastAPI + .NET Aspire Chat Application

A modern chat application built with Vue.js, FastAPI, and .NET Aspire, leveraging LangChain for advanced conversational AI capabilities. The application supports both local development with Ollama and production deployment with Azure OpenAI.

## Why .NET Aspire?

.NET Aspire provides several key benefits for this application:

1. **Unified Orchestration**:
   - Single command to start all services (`dotnet run`)
   - Automatic service discovery and networking
   - Consistent development experience across different platforms

2. **Built-in Monitoring**:
   - Real-time health monitoring through the Aspire dashboard
   - Integrated logging and diagnostics
   - Performance metrics and telemetry

3. **Multi-Language Support**:
   - Seamlessly manages both Python (FastAPI) and Node.js (Vue) applications
   - Handles cross-service communication
   - Environment variable management across services

4. **Production Readiness**:
   - Container orchestration for deployment
   - Load balancing and scaling capabilities
   - Infrastructure as code for cloud deployments

5. **Developer Experience**:
   - Interactive dashboard at http://localhost:15888
   - Live reload and hot module replacement
   - Simplified debugging across services

> 📝 To unlock the power of .NET Aspire, you'll need the .NET SDK, just like you need Python for Jupyter Notebooks. Aspire then enhances your development experience by providing a centralized dashboard for monitoring and managing all the moving parts of your distributed applications, making debugging and troubleshooting a breeze.

## Why LangChain?

This application uses LangChain to provide:

1. **Conversation Memory**: Maintains context across messages using `ConversationBufferMemory`, enabling more coherent and contextual responses.

2. **Flexible Model Integration**: 
   - Local development: Uses Ollama with the Mistral model
   - Production: Seamlessly switches to Azure OpenAI

3. **Advanced Chain Management**: Implements `ConversationChain` for sophisticated conversation handling and state management.

4. **Future Extensibility**: Ready for advanced features like:
   - Document processing and QA
   - Semantic search with embeddings
   - Custom agents for complex tasks
   - Multiple memory types for different use cases

## Prerequisites

- Node.js 20+
- Python 3.11+
- .NET 9.0 SDK
- Docker
- Ollama (for local development)
- Azure OpenAI Service (for production)

## Project Structure

```
├── fastAspire/         # Root project directory
    ├── aspire/         # .NET Aspire orchestration
    ├── backend/        # Python FastAPI backend
        ├── src/        # FastAPI application code
        └── requirements.txt
    └── frontend/       # Vue.js frontend (current directory)
        ├── src/        # Vue source code
        └── public/     # Static assets
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
cd fastAspire/fastAspire.AppHost
dotnet run
```


### Production Deployment

1. Update environment variables for Azure OpenAI
2. Build and deploy using Docker containers

## Features

- Real-time chat interface with memory-enabled responses
- Intelligent conversation management via LangChain
- Environment-aware model selection (Ollama/Azure OpenAI)
- .NET Aspire orchestration for service management
- Health monitoring and logging
- Service discovery and networking

## LangChain Components

The application leverages several key LangChain components:

1. **Memory Management**
- Uses `ConversationBufferMemory` for maintaining chat history
- Enables contextual responses based on previous interactions

2. **Model Integration**
- Local: Ollama with Mistral model for development
- Production: Azure OpenAI for scalable deployment

3. **Conversation Chain**
- Manages message flow and conversation state
- Handles context and memory updates automatically

4. **Environment Awareness**
- Automatically switches between local and production models
- Maintains consistent API regardless of the underlying model
