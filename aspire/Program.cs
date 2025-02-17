var builder = DistributedApplication.CreateBuilder(args);

var backend = builder.AddPythonApp("pythonapp", "../backend")
    .WithHttpEndpoint(containerPort: 8000, hostPort: 8000)
    .WithEnvironment("PYTHONUNBUFFERED", "1");

var frontend = builder.AddNpmApp("vueapp", "../")
    .WithHttpEndpoint(containerPort: 5173, hostPort: 5173)
    .WithReference(backend);

builder.Build().Run();